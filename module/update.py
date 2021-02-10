##!/usr/bin/python
# -*- coding: utf-8 -*-
# Developer by Bafomet

from utils import COLORS

import os
import sys

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
  
'''.format(COLORS.GNSL, COLORS.REDL, COLORS.WHSL)


def update():
    print(page_1)
    option = input(f"{COLORS.REDL} └──>{COLORS.ENDL} Введите 99 для выхода : {COLORS.ENDL} ")
    
    while True:
        if option == '99':
            print()
            print(f"{COLORS.GNSL} [{COLORS.REDL} + {COLORS.GNSL}]{COLORS.WHSL} Спасибо за использование нашего Exploit.")
            return

        elif option == '0':
            print(f"{COLORS.GNSL}[ {COLORS.REDL}+{COLORS.GNSL} ]{COLORS.WHSL} Загрузка с github...{COLORS.ENDL}")
            os.system("git clone https://github.com/Bafomet666/OSINT-SAN")
            os.system("cd ..;python3 osintsan.py")
            return

        else:
            update()


if __name__ == '__main__':
    try:
        update()
    except KeyboardInterrupt:
        print("Ctrl+C pressed...")
        sys.exit(1)
