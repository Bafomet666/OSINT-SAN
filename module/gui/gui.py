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
page_1 = '''{1}
                                                                    
  {0}[ {1}1{0} ] {2}Запуск.       {0}[ {1}0{0} ] {2} Установить зависимости.             
  
'''.format(GNSL, REDL, WHSL)

def main():
    print(page_1)
    print("")
    option = input(REDL + "  └──>" + ENDL +" Введите 1 для запуска сервера : " +ENDL + " ")
    
    while(1):
        if option == '1':
            os.system("cd plugins/gui;python3 geoLRun.py")
            exit()
            option = input(ENDL + ""+GNSL+"["+REDL + " menu " + GNSL + "]"+ENDL + " :")

        elif option == '0':
            print("")
            print(("{1}  [ {0}+{1} ]{2} Происходит установка зависимостей...{3}").format(REDL, GNSL, WHSL, ENDL))
            print("")
            os.system("sudo pip3 install wxPython")
            os.system("cd plugins/gui;python3 geoLRun.py")
            exit()
            break
        else:
            os.system("python3 startadb.py")
try:
    main()

except KeyboardInterrupt:
    sys.exit(1)
except KeyboardInterrupt:
        print ("Ctrl+C pressed...")
