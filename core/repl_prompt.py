# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from utils.banner import show_banner
from utils import COLORS
from prompt_toolkit import prompt
from osintsan import menu

import subprocess
import os
import sys


# Developer by Bafomet
def repl():  # Read\xe2\x80\x93eval\xe2\x80\x93print loop
    while True:
        print(menu())
        user_input = input(" └──>  Выбери опцию : ")
        if len(user_input) == 0:
            print()
            continue
        try:
            choice = int(user_input)
        except ValueError:
            print()
            continue

        if choice == 1:
            from plugins.shodan_io import shodan_host, check_shodan_api
            from plugins.censys import censys_ip

            if not check_shodan_api():
                show_banner(clear=True)
                print(f"{COLORS.REDL}`shodan_api` не валиден, поправь в core/config.py токен!{COLORS.REDL}")
            else:
                print()
                ip = prompt("  └──> Введите IP адрес : ")

                show_banner(clear=True)

                shodan_host(ip)
                censys_ip(ip)

        elif choice == 2:
            from plugins.domain import domain

            host = input(" └──> Введите хостинг либо IP адрес : ")
            port = ""

            while True:
                try:
                    port = input(" └──> Нажми enter, или напиши свой варианта порта : ")
                    port = int(port)
                except ValueError:
                    if port == "":
                        port = 80
                    else:
                        continue

                if port not in [80, 443]:
                    print(" Неверный порт ")
                    continue
                else:
                    break

            domain(host, port)

        elif choice == 3:
            from plugins.Phonenumber import phone_number, check_phone_api_token

            if not check_phone_api_token():
                show_banner(clear=True)
                print(f"{COLORS.REDL}phone api невалиден! (settings.py){COLORS.REDL}")
            else:
                ph = input(" └──> Введи мобильный номер телефона с +7... : ")
                show_banner(clear=True)
                phone_number(ph)

        elif choice == 4:
            from plugins.dnsdump import dnsmap

            print("\n Работает только с (.com .ru)\n")
            dnsmap_inp = prompt("    └──> Введите url : ")

            dnsmap(dnsmap_inp)

            show_banner(clear=True)

        elif choice == 5:
            from plugins.metadata import gps_analyzer

            print("\n   Пример пути: /home/bafomet/Desktop/deanon.png\n")
            img_path = prompt(" └──> Укажите путь до фотографии :")

            show_banner(clear=True)

            gps_analyzer(img_path)

        elif choice == 6:
            from plugins.reverseimagesearch import reverseimagesearch

            print("\n  Пример пути: /home/bafomet/Desktop/deanon.png\n")
            img = prompt(" └──> Укажите путь до фотографии :")

            show_banner(clear=True)

            reverseimagesearch(img)

        elif choice == 7:
            from plugins.honeypot import honeypot

            print()
            hp_inp = prompt(" └──> Введите IP адрес : ")

            show_banner(clear=True)

            honeypot(hp_inp)

        elif choice == 8:
            from plugins.macaddress import MacAddressLookup

            print()
            mac = prompt(" └──> Ожидаю ввод MAC адреса :")

            show_banner(clear=True)

            MacAddressLookup(mac)

        elif choice == 9:
            from module.gui import run_gui

            run_gui()

            show_banner(clear=True)

        elif choice == 10:
            from plugins.torrent import torrent

            print()
            ip_ = prompt(" └──> Введите IP адрес :")

            show_banner(clear=True)

            torrent(ip_)

        elif choice == 11:
            os.system("cd module;python3 main.py")

            show_banner(clear=True)

        elif choice == 12:
            from module.subzone import subzone
            show_banner(clear=True)
            subzone()

        elif choice == 13:
            from plugins.maildb import maildb

            print("\n Пример :google.com\n")
            web = prompt(" └──> Введи домен организации :")
            show_banner(clear=True)

            maildb(web)

        elif choice == 14:
            os.system("cd exploit_database;python3 startadb.py")
            show_banner(clear=True)

        elif choice == 15:
            os.system("cd plugins/Brother;sudo python3 dlc.py -t manual -k start")
            show_banner(clear=True)

        elif choice == 16:
            os.system("cd exploit_database;python3 hynder.py")
            subprocess.call("python3 osintsan.py", shell=True)

        elif choice == 17:
            subprocess.call("sudo etherape", shell=True)
            show_banner(clear=True)

        elif choice == 18:
            os.system("cd module;python3 update.py")

            show_banner(clear=True)

        elif choice == 19:
            subprocess.call(
                "firefox https://github.com/Bafomet666/OSINT-SAN", shell=True
            )

            show_banner(clear=True)

        elif choice == 20:
            os.system("cd exploit_database;python3 subjection.py")
            show_banner(clear=True)

        elif choice == 21:
            os.system("cd module;python3 Information_services.py")
            show_banner(clear=True)

        elif choice == 22:
            os.system("cd exploit_database;sudo ./instashell.sh")
            show_banner(clear=True)

        elif choice == 23:
            os.system("cd exploit_database;python3 error.py")
            show_banner(clear=True)

        elif choice == 24:
            os.system("cd exploit_database;python3 pass.py")
            show_banner(clear=True)

        elif choice == 25:
            os.system("cd plugins/xss;python2 xss.py")

        elif choice == 26:
            os.system("cd exploit_database;python3 bx54.py")
            show_banner(clear=True)

        elif choice == 27:
            os.system("cd exploit_database;python3 domian2.py")
            show_banner(clear=True)

        elif choice == 28:
            subprocess.call("sudo maltego", shell=True)
            show_banner(clear=True)

        elif choice == 29:
            os.system("cd exploit_database;python3 zoom.py")
            show_banner(clear=True)

        elif choice == 30:
            os.system("cd exploit_database;python3 deanon_main.py")
            show_banner(clear=True)

        elif choice == 31:
            os.system("firefox https://canarytokens.org")
            show_banner(clear=True)

        elif choice == 32:
            pass

        elif choice == 33:
            os.system("cd module;python3 whoyous.py")
            show_banner(clear=True)

        elif choice == 34:
            os.system("cd module;python3 leaks.py")
            show_banner(clear=True)

        elif choice == 35:
            os.system("firefox https://search4faces.com")
            os.system("firefox https://findclone.ru")
            os.system("firefox https://images.google.com/")
            os.system("firefox https://yandex.ru/images/")
            os.system("firefox https://tineye.com/")
            os.system("firefox https://pimeyes.com/en/")
            os.system("firefox https://carnet.ai/")
            show_banner(clear=True)

        elif choice == 36:
            os.system("cd module;python3 osint_pack.py")
            show_banner(clear=True)

        elif choice == 37:
            os.system("cd plugins/webvuln/src/tisyka;python3 bx66.py")
            show_banner(clear=True)

        elif choice == 38:
            os.system("firefox https://temp-mail.org/ru/")
            os.system("firefox https://10minemail.com/ru/")
            os.system("firefox https://10minutemail.net/?lang=ru")
            os.system("firefox https://www.lite14.us/10minutemail/russian.html")
            os.system("firefox https://protonmail.com/ru/")
            os.system("firefox https://tutanota.com/ru/blog/posts/anonymous-email/")
            show_banner(clear=True)

        elif choice == 39:
            os.system("cd plugins/Brother;sudo python3 dlc2.py -t manual -k start")
            show_banner(clear=True)

        elif choice == 40:
            pass

        elif choice == 41:
            os.system("cd module;python3 avito.py")

        elif choice == 44:
            os.system("firefox https://t.me/osint_san_framework")
            os.system("firefox https://github.com/Bafomet666/OSINT-SAN")
            show_banner(clear=True)

        elif choice == 45:
            os.system("cd module;python3 license_agreement.py")
            show_banner(clear=True)

        elif choice == 66:
            show_banner(clear=True)

        elif choice == 99:
            os.system("python3 osintsan.py")

        elif choice == 88:
            from core.core import main

            main()

        elif choice == 0:
            print(" Спасибо что использовали наш Framework...")
            sys.exit()

        else:
            pass


try:
    repl()
except KeyboardInterrupt:
    os.system("clear")
    sys.exit()
