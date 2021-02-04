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
os.system("printf '\033]2;OSINT Биржа\a'")
os.system('clear')
page_1 = '''{1}

                                    $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ $$$$$$$$\        $$$$$$\   $$$$$$\  $$\   $$\ 
                                   $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |\__$$  __|      $$  __$$\ $$  __$$\ $$$\  $$ |
                                   $$ /  $$ |$$ /  \__|  $$ |  $$$$\ $$ |   $$ |         $$ /  \__|$$ /  $$ |$$$$\ $$ |
                                   $$ |  $$ |\$$$$$$\    $$ |  $$ $$\$$ |   $$ |         \$$$$$$\  $$$$$$$$ |$$ $$\$$ |
                                   $$ |  $$ | \____$$\   $$ |  $$ \$$$$ |   $$ |          \____$$\ $$  __$$ |$$ \$$$$ |
                                   $$ |  $$ |$$\   $$ |  $$ |  $$ |\$$$ |   $$ |         $$\   $$ |$$ |  $$ |$$ |\$$$ |
                                    $$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |   $$ |         \$$$$$$  |$$ |  $$ |$$ | \$$ |
                                    \______/  \______/ \______|\__|  \__|   \__|          \______/ \__|  \__|\__|  \__|
                                                                                                                                                                                                                    
  Ожидайте в следующем обновлении.

  {0}[ {1}99{0} ] {2}Пойти нахуй...                 
  
'''.format(GNSL, REDL, WHSL)

def main():
    print(page_1)
    option = input(REDL + "  └──>" + ENDL +" Введите 99 для выхода : " +ENDL + " ")
    
    while(1):
        if option == '99':
            print("")
            print(("{1} [{0} + {1}]{2} Спасибо за использование нашего Exploit.").format(REDL, GNSL, WHSL))
            os.system("cd ..;python3 osintsan.py")
            exit()
            option = input(ENDL + ""+GNSL+"["+REDL + " menu " + GNSL + "]"+ENDL + " :")


        else:
            os.system("avito.py")
try:
    main()

except KeyboardInterrupt:
    sys.exit(1)
except KeyboardInterrupt:
        print ("Ctrl+C pressed...")
