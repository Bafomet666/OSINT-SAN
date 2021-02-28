##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
from module.utils import COLORS

import os
import sys

page_1 = '''{1}


   ██████╗ ███████╗██╗███╗   ██╗████████╗    ██╗███╗   ██╗███████╗ ██████╗ 
  ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██║████╗  ██║██╔════╝██╔═══██╗
  ██║   ██║███████╗██║██╔██╗ ██║   ██║       ██║██╔██╗ ██║█████╗  ██║   ██║
  ██║   ██║╚════██║██║██║╚██╗██║   ██║       ██║██║╚██╗██║██╔══╝  ██║   ██║
  ╚██████╔╝███████║██║██║ ╚████║   ██║       ██║██║ ╚████║██║     ╚██████╔╝
   ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                                                                                               
{0}    Выгрузка материала  

    А что ты думал ? я здесь дохрена распишу информации Джони ? Нет, тут просто загрузка доп материалов по осинту.
    
    После загрузки, пиздуй в папку osint-info там лежит твое добро.

  {0}[ {1}99{0} ] {2}Пойти нахуй...       {0}[ {1}0{0} ] {2} Загрузить mini pack...                  
  
'''.format(COLORS.GNSL, COLORS.REDL, COLORS.WHSL)


def osint_pack():
    os.system("printf '\033]2;OSINT INFO\a'")
    os.system('clear')

    print(page_1)

    while True:
        try:
            option = input(f"{COLORS.REDL}  └──>{COLORS.ENDL} Введите 99 для выхода : {COLORS.ENDL} ")
        except KeyboardInterrupt:
            option = "99"

        if option == '99':
            print()
            print(f"{COLORS.GNSL}[{COLORS.REDL}+{COLORS.GNSL}]{COLORS.WHSL} Спасибо за использование нашего Exploit.")
            return

        elif option == '0':
            print()
            print(f"{COLORS.GNSL}[ {COLORS.REDL}+{COLORS.GNSL} ]{COLORS.WHSL} Загрузка с github...{COLORS.ENDL}")
            os.system("git clone https://github.com/Bafomet666/osint-info")
            return

        else:
            continue


if __name__ == '__main__':
    try:
        osint_pack()
    except KeyboardInterrupt:
        print("Ctrl+C pressed...")
        sys.exit(1)
