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
    
{1}      /$$$$$$                  /$$                     /$$       /$$      
{1}     /$$__  $$                | $$                    |__/      | $$      
{1}    | $$  \ $$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$  /$$$$$$$      
{1}    | $$$$$$$$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$ /$$__  $$
{1}    | $$__  $$| $$  \ $$| $$  | $$| $$  \__/| $$  \ $$| $$| $$  | $$      
{1}    | $$  | $$| $$  | $$| $$  | $$| $$      | $$  | $$| $$| $$  | $$      
{1}    | $$  | $$| $$  | $$|  $$$$$$$| $$      |  $$$$$$/| $$|  $$$$$$$      
{1}    |__/  |__/|__/  |__/ \_______/|__/       \______/ |__/ \_______/                                                      
                                                                          
{1}                                                                   /$$    
{1}                                                                  | $$    
{1}      /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$  
{1}     /$$_____/ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$_____/|_  $$_/  
{1}    | $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$        | $$    
{1}    | $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/| $$        | $$ /$$
{1}    |  $$$$$$$|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$$|  $$$$$$$  |  $$$$/
{1}     \_______/ \______/ |__/  |__/|__/  |__/ \_______/ \_______/   \___/  
                                                                          
     {0}Изучай как работaет соендинение adb.{1}    
     {0}Обязательно установи зависимости.
     {0}Ты можешь открыть кнопкой 5 сайты с подробным описанием по подключению adb.{1}     
                                                                               
    
     {0}[ {1}1{0} ] {2}Запуск.   {0}[ {1}1{0} ] {2}Установить зависимости.  {0}[ {1}5{0} ] {2}Полный гайд.
    """.format(
            GNSL, REDL, WHSL
        )
    )


def main():
    android_banner()
    print()
    option = input(f"{REDL}     └──>{ENDL} Введите 1 для запуска сервера : {ENDL} ")

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
