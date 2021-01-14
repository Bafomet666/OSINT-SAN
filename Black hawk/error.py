#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
import sys
import readline
import subprocess
# set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

page = '''{1} {1} 
 
  {0} ██████╗ ███████╗██╗███╗   ██╗████████╗    ███████╗ █████╗ ███╗   ██╗{0}     {2} Dev Bafomet {2}
  {0}██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██╔════╝██╔══██╗████╗  ██║{0}     {2} Разработано для диванных кибер армий СНГ {2}
  {0}██║   ██║███████╗██║██╔██╗ ██║   ██║       ███████╗███████║██╔██╗ ██║{0}     {2} Во славу и честь, за сиськи и минет...   {2}
  {0}██║   ██║╚════██║██║██║╚██╗██║   ██║       ╚════██║██╔══██║██║╚██╗██║{0}     
  {0}╚██████╔╝███████║██║██║ ╚████║   ██║       ███████║██║  ██║██║ ╚████║{0} 
  {0} ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝{0}    
  
  {2} Список бесплатных средств анонимизации: VPN, Proxy

  {2} Перед использованием эксплойта, обезопась себя и своих близких... {2}
  
  {1} Для браузеров. {1}
                     
                  {0} https://addons.mozilla.org/ru/firefox/addon/browsec/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search {0} 
                     
                  {0} https://addons.mozilla.org/ru/firefox/addon/hide-my-ip-vpn/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search {0} 
                     
                  {0} https://addons.mozilla.org/ru/firefox/addon/urban-vpn/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search {0} 
                     
                  {0} Но помни они тебе не обеспечат 100% безопасности, браузерные только для серфинга.  {0} 

  {1} Списки репозиториев.{1} linux
  
                  {0} https://github.com/apify/proxy-chain  {0} 
 
                  {0} https://github.com/Und3rf10w/kali-anonsurf  {0} 

                  {0} https://github.com/SusmithKrishnan/torghost  {0} 
                      
  {1} Бесплатные сервисы. {1}
      
                 {0} https://www.vpnbook.com/freevpn  {0} 
 
                 {0} https://www.vpngate.net/en/  {0} 
                 
  {1} Списки репозиториев.{1} Windows.
  
                 {0} https://rus.windscribe.com/download  {0}

                                           {0} Некоторые vpn и proxy не сохранят вашу анонимность на 100% , лучше делать цепочки.
  
  {0}[ {1}1{0} ] {2}Выйти в главное меню...                
  
'''.format(GNSL, REDL, WHSL)
def main(): 
    option = input(REDL + " └──>" + ENDL + " Введите 1 для выхода : "+ENDL + " ") 
    while(1):
        if option == '1':
            print(("{1}[{0}+{1}]{2} Спасибо за использование нашего Exploit.").format(REDL, GNSL, WHSL))
            subprocess.call("python3 osintsan.py", shell=True)
            exit()
            option = input(ENDL + ""+GNSL+"("+REDL + " menu " + GNSL + ")"+ENDL + "> ")

os.system("printf '\033]2;OSINT SAN [ OSINT service ]\a'")
os.system('clear')
print(page)
main()
