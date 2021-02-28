##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import multiprocessing
from module.utils import COLORS
import sys


def main():
    print(f"{COLORS.REDL} Запуск консольного приложения...{COLORS.ENDL}")
    from module.gui import geoLRun

    multiprocessing.Process(target=geoLRun.main).start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl+C pressed...")
        sys.exit(1)
