#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
import sys
import readline
import random
import time as  t


WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'
load_count = 0
page2 = False

arrow = REDL + "└──>" + WHSL
arrow = str(" "+arrow)
connect = REDL + "│" + WHSL

page_1 = '''{1}

                                        ______    ______   ______  __    __  ________         ______    ______   __    __            
                                       /      \  /      \ |      \|  \  |  \|        \       /      \  /      \ |  \  |  \           
                                      |  $$$$$$\|  $$$$$$\ \$$$$$$| $$\ | $$ \$$$$$$$$      |  $$$$$$\|  $$$$$$\| $$\ | $$           
                                      | $$  | $$| $$___\$$  | $$  | $$$\| $$   | $$         | $$___\$$| $$__| $$| $$$\| $$           
                                      | $$  | $$ \$$    \   | $$  | $$$$\ $$   | $$          \$$    \ | $$    $$| $$$$\ $$           
                                      | $$  | $$ _\$$$$$$\  | $$  | $$\$$ $$   | $$          _\$$$$$$\| $$$$$$$$| $$\$$ $$           
                                      | $$__/ $$|  \__| $$ _| $$_ | $$ \$$$$   | $$         |  \__| $$| $$  | $$| $$ \$$$$           
                                       \$$    $$ \$$    $$|   $$ \| $$  \$$$   | $$          \$$    $$| $$  | $$| $$  \$$$           
                                        \$$$$$$   \$$$$$$  \$$$$$$ \$$   \$$    \$$           \$$$$$$  \$$   \$$ \$$   \$$           
                                                                                               
                                                                                               
                                                                 {2}Добро пожаловать самурай.{0}
                                                                      
                                                                      
                            Ожидайте в следующем обновлении анонимный чат в самом OSINT SAN. Но для большого количества людей в комнатах, мы зальем его на git.
  
                        {2}Официальные источники продукта:{2}
                            
                            {0}Telegram:{1} https://t.me/osint_san_framework
                            {0}Github:{1} https://github.com/Bafomet666/OSINT-SAN
                                                                                                          
                                                          
  {0}[ {1}1{0} ] {2}Выйти в главное меню...                
  
'''.format(GNSL, REDL, WHSL)




page_2 = '''\n
'''.format(GNSL, REDL, WHSL)

def main():
    print (("\n{1}[ {0}+{1} ]{2} Спасибо за использование нашего эксплойта...").format(REDL, GNSL, WHSL))
    page_num = 1
    option = input(ENDL + "  └──> Введите 1 для выхода : "+ENDL + " ")
        
    while(1):
        
        if option == '1':
            print(("{1}[{0}+{1}]{2} Спасибо за использование нашего Exploit.").format(REDL, GNSL, WHSL))
            subprocess.call("python3 osintsan.py", shell=True)
            t.sleep(4)
            exit()
            option = input(ENDL + ""+GNSL+"("+REDL + " menu " + GNSL + ")"+ENDL + "> ")

    main()
import subprocess
import os
os.system("printf '\033]2;Соглашение...\a'")
t.sleep(4)
os.system('clear')
print(page_1)
main()
