##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import subprocess
import os
import sys
import readline
#set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'
os.system("printf '\033]2;OSINT Update\a'")
os.system('clear')
page_1 = '''{1}
 {1}{0}[{2} Official channel {0}tg {1}@osint_san_framework {1}{0}]                {0}[{2} GitHub {1}https://github.com/Bafomet666 {1}{0}]            {0}[ {1}R{2} патч 3.1 {1}{0}]

{0}                                    _______   ________  _______          ______    ______   ______  __    __  ________  {1}     __    __ 
{0}                                   /       \ /        |/       \        /      \  /      \ /      |/  \  /  |/        | {1}    /  |  /  |
{0}                                   $$$$$$$  |$$$$$$$$/ $$$$$$$  |      /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \ $$ |$$$$$$$$/  {1}    $$ |  $$ |
{0}                                   $$ |__$$ |$$ |__    $$ |  $$ |      $$ |  $$ |$$ \__$$/   $$ |  $$$  \$$ |   $$ |    {1}    $$  \/$$/ 
{0}                                   $$    $$< $$    |   $$ |  $$ |      $$ |  $$ |$$      \   $$ |  $$$$  $$ |   $$ |    {1}      $$  $$<  
{0}                                   $$$$$$$  |$$$$$/    $$ |  $$ |      $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |    {1}      $$$$  \ 
{0}                                   $$ |  $$ |$$ |_____ $$ |__$$ |      $$ \__$$ |/  \__$$ | _$$ |_ $$ |$$$$ |   $$ |    {1}     $$ /$$  |
{0}                                   $$ |  $$ |$$       |$$    $$/       $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |    {1}    $$ |  $$ |
{0}                                   $$/   $$/ $$$$$$$$/ $$$$$$$/         $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/     {1}    $$/   $$/ 
                                                                                                                                                                                                                                                                                                                                                                                                                     
 {2}Framework :{2}{0} OSINT SAN.{0}
 {2}Update{0} RED Alert v-3.0
 
 {2}Список изменений обновлений и инструкция по установке...   

 {0}Обновление загружается ввиде папки, После вам нужно скопировать все из папки update-osint
 в папку с самим эксплойтом OsintSan с заменой файлов.

 Но возможно могут слететь ваши API, заранее прошу извинения.
 Обновления выходят раз в месяц. Патчи могут выходить раз в две недели.

 {2}Дата последнего обновления 10 февраля.           

 {0}[ {1}99{0} ] {2}Выйти...       {0}[ {1}0{0} ] {2} Загрузить обновление...                  
  
'''.format(GNSL, REDL, WHSL)

def main():
    print(page_1)
    option = input(REDL + " └──>" + ENDL +" Введите 99 для выхода : " +ENDL + " ")
    
    while(1):
        if option == '99':
            print("")
            print(("{1} [{0} + {1}]{2} Спасибо за использование нашего Exploit.").format(REDL, GNSL, WHSL))
            os.system("exit")
            exit()
            option = input(ENDL + ""+GNSL+"["+REDL + " menu " + GNSL + "]"+ENDL + " :")

        elif option == '0':
            print(("{1}[ {0}+{1} ]{2} Загрузка с github...{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("git clone https://github.com/Bafomet666/OSINT-SAN")
            os.system("cd ..;python3 osintsan.py")
            exit()
            break
        else:
            os.system("python3 update.py")
try:
    main()

except KeyboardInterrupt:
    sys.exit(1)
except KeyboardInterrupt:
        print ("Ctrl+C pressed...")
