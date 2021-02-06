##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
from utils import COLORS
import sys


def main():
    print(f"{COLORS.REDL} Запуск консольного приложения...{COLORS.ENDL}")
    from module.gui import geoLRun

    geoLRun.main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl+C pressed...")
        sys.exit(1)
