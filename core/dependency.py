import os
from dataclasses import dataclass

import shutil
import platform


@dataclass
class Dependency:
    name: str

    def installed(self) -> bool:
        return NotImplemented

    def uninstalled_info_message(self) -> str:
        raise NotImplemented


class Api(Dependency):
    def installed(self) -> bool:
        return bool(self.name)

    def uninstalled_info_message(self) -> str:
        return f"{self.name} токен не установлен! (скорее всего, он находится в settings.py)"


class Package(Dependency):
    def installed(self) -> bool:
        return bool(shutil.which(self.name))

    def uninstalled_info_message(self) -> str:
        return f"{self.name} не найден в системе."


class Platform(Dependency):
    # Could be only 'Linux', 'Darwin', 'Java', 'Windows'
    def installed(self) -> bool:
        return platform.system() in self.name.split("|")

    def uninstalled_info_message(self) -> str:
        return f"{platform.system()} не поддерживается, для этого модуля нужен {self.name}."

    def __add__(self, other: "Platform") -> "Platform":
        return Platform(f"{self.name}|{other.name}")


class Permission(Dependency):
    # could be only 'user' or 'root'
    def installed(self) -> bool:
        return self.name != "root" or os.getuid() == 0

    def uninstalled_info_message(self) -> str:
        return "Плагин запущен не под root'ом!"
