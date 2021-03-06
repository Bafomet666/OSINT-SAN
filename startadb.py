##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
import sys
import webbrowser
from module import android_debug

#set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'


def android_banner():
    os.system("printf '\033]2;OSINT-SAN 3.5\a'")
    os.system("clear")
    print(
        """{1}
     {2} Советы при использовании.
     
     {0} При подключении через shell, управлять переходами по директории устройств можно командами
      cd,ls, для выхода exit

     {0} При выходе из инструмента обязательно отключайте сервера командой 88, если этого не сделать,
     {0} это приведет к вашей деанонимизации.

     {0} Ищите новые устройства через shodan или zoomeye.
     {0} Инструменты по поиску можно найти в главное меню.
                                                                               
    
     {0}[ {1}1{0} ] {2}Запутить   {0}[ {1}1{0} ] {2}Установить зависимости.  {0}[ {1}5{0} ] {2}Открыть гайды.
    """.format(
            GNSL, REDL, WHSL
        )
    )


def main():
    android_banner()
    print()
    option = input(f"{REDL}     └──>{ENDL} Введите опцию : {ENDL} ")

    while True:
        if option == "1":
            android_debug.android_debug()
            break

        elif option == "0":
            print()
            print(
                ("{1}  [ {0}+{1} ]{2} Происходит установка зависимостей...{3}").format(
                    REDL, GNSL, WHSL, ENDL
                )
            )
            print()
            os.system("sudo apt-get install adb")
            os.system("sudo apt-get install android-tools-adb")
            os.system("sudo apt install android-tools-adb android-tools-fastboot")
            android_debug.android_debug()
            break
        elif option == "5":
            urls = [
                "http://android-tip.com/soveti_i_poleznoe/77-adb-dlya-chaynikov-chast-1.html",
                "https://irongamers.ru/forum/faq/izuchaem-android-desjat-osnovnyh-komand-adb-i-fastboot-kotorye-vy-dolzhny-znat-d",
                "https://docs.microsoft.com/ru-ru/dual-screen/android/emulator/adb",
                "https://softandroid.net/2020/01/05/adb-%D0%B8%D0%BB%D0%B8-android-debug-bridge-%D0%BE%D0%B1%D1%8A%D1%8F%D1%81%D0%BD%D1%8F%D1%8E-%D0%BD%D0%B0-%D0%BF%D0%B0%D0%BB%D1%8C%D1%86%D0%B0%D1%85-%D1%87%D1%82%D0%BE-%D1%8D%D1%82%D0%BE-%D0%B7/",
                "https://www.youtube.com/watch?v=QOXmNDXDWhM", 
            ]
            for url in urls:
                webbrowser.open(url)
            main()
            break
        else:
            main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl+C pressed...")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Ctrl+C pressed...")
        sys.exit(1)
