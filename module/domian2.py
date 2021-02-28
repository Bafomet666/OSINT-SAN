#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
from datetime import datetime
import socket
import requests

# Set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

page = """
\033[1;34m [\033[0;31m 1 \033[1;34m] \033[1;32m  Whois Lookup       \033[1;34m[\033[0;31m 8  \033[1;34m] \033[1;32m   HTTP Header                  
\033[1;34m [\033[0;31m 2 \033[1;34m] \033[1;32m  Просмотреть DNS    \033[1;34m[\033[0;31m 9  \033[1;34m] \033[1;32m   Host Finder
\033[1;34m [\033[0;31m 3 \033[1;34m] \033[1;32m  GeoIP Lookup       \033[1;34m[\033[0;31m 10 \033[1;34m] \033[1;32m   IP геолокация   
\033[1;34m [\033[0;31m 4 \033[1;34m] \033[1;32m  Subnet Lookup      \033[1;34m[\033[0;31m 11 \033[1;34m] \033[1;32m   Найти общие DNS-серверы 
\033[1;34m [\033[0;31m 5 \033[1;34m] \033[1;32m  Port сканер        \033[1;34m[\033[0;31m 12 \033[1;34m] \033[1;32m   Get Robots.txt   
\033[1;34m [\033[0;31m 6 \033[1;34m] \033[1;32m  Ссылки на страницу \033[1;34m[\033[0;31m 13 \033[1;34m] \033[1;32m   Host DNS Finder
\033[1;34m [\033[0;31m 7 \033[1;34m] \033[1;32m  Зона передачи      \033[1;34m[\033[0;31m 14 \033[1;34m] \033[1;32m   Выйти
               
          
          """


def domain():
    while True:

        print()
        try:
            website = input(
                f"{WHSL} └──> Я жду от тебя ввод сайта{GNSL}[ {REDL}main_menu{GNSL} ]{ENDL} :"
            )
            print(page)
            valorselec = input(f"{WHSL} └──> Выбери опцию{GNSL}[ {REDL}main_menu{GNSL} ]{ENDL} :")

        except KeyboardInterrupt:
            return

        if valorselec == "14":
            return

        valorselec_to_url = {
            "1": "https://api.hackertarget.com/whois/?q={website}",
            "2": "https://api.hackertarget.com/dnslookup/?q={website}",
            "3": "http://api.hackertarget.com/geoip/?q={website}",
            "4": "http://api.hackertarget.com/subnetcalc/?q={website}",
            "5": "https://api.hackertarget.com/nmap/?q={website}",
            "6": "https://api.hackertarget.com/pagelinks/?q={website}",
            "7": "https://api.hackertarget.com/zonetransfer/?q={website}",
            "8": "https://api.hackertarget.com/httpheaders/?q={website}",
            "9": "https://api.hackertarget.com/hostsearch/?q={website}",
            "10": "https://ipinfo.io/{website}/json",
            "11": "https://api.hackertarget.com/findshareddns/?q={website}",
            "12": "http://{website}/robots.txt",
            "13": "https://api.hackertarget.com/mtr/?q={website}",
        }
        url = valorselec_to_url.get(valorselec)
        if not url:
            pass

        url = url.format(website=website)

        try:
            info = requests.get(url)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text)
        except (UnboundLocalError, socket.gaierror):
            pass

        except requests.exceptions.ConnectionError:
            return


def record_resalt(resalt):
    now = datetime.now()
    data_time = "{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute)
    
    with open('resalt_modul_27.txt', 'a') as file:
        file.write(f'\n{"-"*30}\n\n{data_time}\n\n{resalt}\n')
