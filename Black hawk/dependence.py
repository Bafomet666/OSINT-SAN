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

page_1 = '''{2}
 
  ██████╗ ███████╗██╗███╗   ██╗████████╗    ███████╗ █████╗ ███╗   ██╗
 ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██╔════╝██╔══██╗████╗  ██║
 ██║   ██║███████╗██║██╔██╗ ██║   ██║       ███████╗███████║██╔██╗ ██║
 ██║   ██║╚════██║██║██║╚██╗██║   ██║       ╚════██║██╔══██║██║╚██╗██║
 ╚██████╔╝███████║██║██║ ╚████║   ██║       ███████║██║  ██║██║ ╚████║
  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ {2}

Не обновлялось с альфы. Зайди на github -- https://github.com/Bafomet666/OSINT-SAN

{2}Зависимости обязательные к установке. {2}
{0}
     -- sudo apt install python3

     -- sudo apt install python3-pip. {0}
     
{2}Зависимости для Android Debug Bridge. {2}
{0}
     -- sudo apt-get install adb

     -- sudo apt update

     -- sudo apt-get install android-tools-adb

     -- sudo apt install android-tools-adb android-tools-fastboot
     
     -- sudo pip3 install pip --upgrade

     -- sudo pip3 install setuptools --upgrade
{0}
{2}Основная ветка зависимостей. {2}
{0}
     -- sudo python3 -m pip install urllib3
    
     -- sudo pip3 install h8mail
 
     -- sudo apt-get install wget

     -- sudo pip3 install paramiko

     -- sudo apt install whois

     -- sudo pip3 install gmplot

     -- sudo pip3 install lxml
     
     -- sudo pip3 install Pillow
     
     -- sudo pip3 install pythonping
     
     -- sudo pip3 install beautifulsoup4
     
     -- sudo pip3 install shodan
     
     -- sudo pip3 install requests
     
     -- sudo pip3 install click
     
     -- sudo apt-get install nmap

     -- sudo apt install etherape 
    
     -- sudo apt update {0}
     
     -- pip install subprocess.run
     
     -- pip3 install wxPython
 
  {2}Зависимость для Big Bro. {2}

 {1} ngrok. {1}

        {2}   Оф сайт: {2} {1} https://ngrok.com/download  {1}
 
 {2} Видеогайды по установке ngrok {2}{1} 1 https://www.youtube.com/watch?v=xkxsXLH8iKs {1}

                                      {1} 2 https://www.youtube.com/watch?v=cQhnE_PORgg {1}

  {2}Гайд по установке :{2} {1}   https://kali.tools/?p=5489 {1}
  
     
{2}  У вас может быть разный pip при установке. Но ставить все и запускать надо на python3 {2}
{2}  eсли вдруг установка не прошла, копируйте нужный вам модуль, и гуглите установку. {2}


  {0}[ {1}1{0} ] {2}Выйти в главное меню...                
  
'''.format(GNSL, REDL, WHSL)




page_2 = '''\n
'''.format(GNSL, REDL, WHSL)

def main():
    print (("\n{1}[ {0}+{1} ]{2} Спасибо за использование нашего эксплойта...").format(REDL, GNSL, WHSL))
    os.system("")
    os.system("")
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
os.system("printf '\033]2;Список инструментов /OSINT по русски..\a'")
t.sleep(4)
os.system('clear')
print(page_1)
main()
