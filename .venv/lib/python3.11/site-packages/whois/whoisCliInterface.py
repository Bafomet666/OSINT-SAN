#!  /usr/bin/env python3

import subprocess
import time

# import sys
import os
import platform
import shutil
import logging

from typing import (
    List,
)

from .exceptions import (
    WhoisCommandFailed,
    WhoisCommandTimeout,
)

from .context.parameterContext import ParameterContext
from .context.dataContext import DataContext

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


class WhoisCliInterface:
    def _specificOnNonWindowsPlatforms(self) -> None:
        self.IS_WINDOWS: bool = platform.system() == "Windows"
        self.STDBUF_OFF_CMD: List[str] = []
        if not self.IS_WINDOWS and shutil.which("stdbuf"):
            self.STDBUF_OFF_CMD = ["stdbuf", "-o0"]

    def __init__(
        self,
        pc: ParameterContext,
        dc: DataContext,
    ):
        self.dc = dc
        self.pc = pc

    def _tryInstallMissingWhoisOnWindows(self) -> None:
        """
        Windows 'whois' command wrapper
        https://docs.microsoft.com/en-us/sysinternals/downloads/whois
        """
        folder = os.getcwd()
        copy_command = r"copy \\live.sysinternals.com\tools\whois.exe " + folder
        msg = "downloading dependencies: {copy_command}"
        log.debug(msg)

        subprocess.call(
            copy_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
        )

    def _onWindowsFindWhoisCliAndInstallIfNeeded(self, k: str) -> None:
        paths = os.environ["path"].split(";")
        for path in paths:
            wpath = os.path.join(path, k)
            if os.path.exists(wpath):
                self.pc.cmd = wpath  # note we update cmd if we find one
                return

        if self.pc.tryInstallMissingWhoisOnWindows:
            self._tryInstallMissingWhoisOnWindows()

    def _makeWhoisCommandToRunWindows(
        self,
        whoisCommandList: List[str],
    ) -> List[str]:
        if self.pc.cmd == "whois":  # the default string
            k: str = "whois.exe"
            if os.path.exists(k):
                self.pc.cmd = os.path.join(".", k)
            else:
                self._onWindowsFindWhoisCliAndInstallIfNeeded(k)

        whoisCommandList = [self.pc.cmd]

        if self.pc.server:
            return whoisCommandList + ["-v", "-nobanner", self.domain, self.pc.server]
        return whoisCommandList + ["-v", "-nobanner", self.domain]

    def _makeWhoisCommandToRun(self) -> List[str]:
        whoisCommandList: List[str] = [self.pc.cmd]
        if " " in self.pc.cmd:
            whoisCommandList = self.pc.cmd.split(" ")

        if self.IS_WINDOWS:
            return self._makeWhoisCommandToRunWindows(
                whoisCommandList=whoisCommandList,
            )

        if self.pc.extractServers:
            whoisCommandList = whoisCommandList + ["--verbose"]

        if self.pc.server:
            whoisCommandList = whoisCommandList + ["-h", self.pc.server]

        return whoisCommandList + [self.domain]

    def _postProcessingResult(self) -> str:
        msg = f"{self.rawWhoisResultString}"
        log.debug(msg)

        if self.pc.ignore_returncode is False and self.processHandle.returncode not in [0, 1]:
            if "fgets: Connection reset by peer" in self.rawWhoisResultString:
                return self.rawWhoisResultString.replace("fgets: Connection reset by peer", "")

            if "connect: Connection refused" in self.rawWhoisResultString:
                return self.rawWhoisResultString.replace("connect: Connection refused", "")

            if self.pc.simplistic:
                return self.rawWhoisResultString

            raise WhoisCommandFailed(self.rawWhoisResultString)

        return str(self.rawWhoisResultString)

    def _runWhoisCliOnThisOs(self) -> str:
        # LANG=en is added to make the ".jp" output consisent across all environments
        # STDBUF_OFF_CMD needed to not lose data on kill

        with subprocess.Popen(
            self.STDBUF_OFF_CMD + self._makeWhoisCommandToRun(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env={"LANG": "en"} if self.domain.endswith(".jp") else None,
        ) as self.processHandle:
            msg = f"timout: {self.pc.timeout}"
            log.debug(msg)

            try:
                self.rawWhoisResultString = self.processHandle.communicate(
                    timeout=self.pc.timeout,
                )[
                    0
                ].decode(errors="ignore")
            except subprocess.TimeoutExpired as ex:
                # Kill the child process & flush any output buffers
                self.processHandle.kill()
                self.rawWhoisResultString = self.processHandle.communicate()[0].decode(errors="ignore")
                # In most cases whois servers returns partial domain data really fast
                # after that delay occurs (probably intentional) before returning contact data.
                # Add this option to cover those cases
                if not self.pc.parse_partial_response or not self.rawWhoisResultString:
                    msg = f"timeout: query took more then {self.pc.timeout} seconds"
                    raise WhoisCommandTimeout(msg) from ex

            return self._postProcessingResult()

    def _returnWhoisPythonFromStaticTestData(self) -> str:
        testDir = os.getenv("TEST_WHOIS_PYTHON")

        pathToTestFile = f"{testDir}/{self.domain}/input"
        if os.path.exists(pathToTestFile):
            with open(pathToTestFile, mode="rb") as f:  # switch to binary mode as that is what Popen uses
                # make sure the data is treated exactly the same as the output of Popen
                return f.read().decode(errors="ignore")

        raise WhoisCommandFailed("")

    # public

    def init(self) -> None:
        self.domain: str = ".".join(self.dc.dList)
        self._specificOnNonWindowsPlatforms()

    def executeWhoisQueryOrReturnFileData(self) -> str:
        # if getenv[TEST_WHOIS_PYTON] then
        #   fake whois by reading static data from a file
        #     this way we can actually implemnt a test run
        #       with known data in and expected data out
        if os.getenv("TEST_WHOIS_PYTHON"):
            return self._returnWhoisPythonFromStaticTestData()

        # slow down before so we can force individual domains at a slower tempo
        if self.pc.slow_down:
            time.sleep(self.pc.slow_down)

        return self._runWhoisCliOnThisOs()
