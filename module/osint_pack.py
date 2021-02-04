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
os.system("printf '\033]2;OSINT INFO\a'")
os.system('clear')
page_1 = '''{1}


   ██████╗ ███████╗██╗███╗   ██╗████████╗    ██╗███╗   ██╗███████╗ ██████╗ 
  ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██║████╗  ██║██╔════╝██╔═══██╗
  ██║   ██║███████╗██║██╔██╗ ██║   ██║       ██║██╔██╗ ██║█████╗  ██║   ██║
  ██║   ██║╚════██║██║██║╚██╗██║   ██║       ██║██║╚██╗██║██╔══╝  ██║   ██║
  ╚██████╔╝███████║██║██║ ╚████║   ██║       ██║██║ ╚████║██║     ╚██████╔╝
   ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                                                                                               
{0}    Выгрузка материала  

    А что ты думал ? я здесь дохрена распишу информации Джони ? Нет, тут просто загрузка доп материалов по осинту.
    
    После загрузки, пиздуй в папку module там лежит твое добро.

  {0}[ {1}99{0} ] {2}Пойти нахуй...       {0}[ {1}0{0} ] {2} Загрузить mini pack...                  
  
'''.format(GNSL, REDL, WHSL)

def main():
    print(page_1)
    option = input(REDL + "  └──>" + ENDL +" Введите 99 для выхода : " +ENDL + " ")
    
    while(1):
        if option == '99':
            print("")
            print(("{1}[{0}+{1}]{2} Спасибо за использование нашего Exploit.").format(REDL, GNSL, WHSL))
            os.system("cd ..;python3 osintsan.py")
            exit()
            option = input(ENDL + ""+GNSL+"["+REDL + " menu " + GNSL + "]"+ENDL + " :")

        elif option == '0':
            print("")
            print(("{1}[ {0}+{1} ]{2} Загрузка с github...{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("git clone https://github.com/Bafomet666/osint-info")
            os.system("cd ..;python3 osintsan.py")
            exit()
            break
        else:
            os.system("osint_pack.py")
try:
    main()

except KeyboardInterrupt:
    sys.exit(1)
except KeyboardInterrupt:
        print ("Ctrl+C pressed...")
