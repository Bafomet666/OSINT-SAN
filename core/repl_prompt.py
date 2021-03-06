# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from module.utils.banner import show_banner
from module.utils import COLORS
from osintsan import menu
from plugins.maildb import maildb
from prompt_toolkit import prompt


import subprocess
import os
import webbrowser


# Developer by Bafomet
def repl():  # Read\xe2\x80\x93eval\xe2\x80\x93print loop
    while True:
        print(menu())

        choice = None
        while True:
            try:
                user_input = input(f"{COLORS.GNSL} └──>  Выберите опцию : {COLORS.ENDL}")
                print()
            except KeyboardInterrupt:
                return

            if len(user_input) == 0:
                os.system("clear")
                break

            try:
                choice = int(user_input)
            except ValueError:
                print(f"{COLORS.REDL}Неверный ввод!{COLORS.ENDL}")
            else:
                break

        if choice is None:
            continue

        if choice == 1:
            from plugins.shodan_io import shodan_host, check_shodan_api
            from plugins.censys import censys_ip

            if not check_shodan_api():
                show_banner(clear=True)
                print(f"{COLORS.REDL}API ключ Shodan'а невалиден! (settings.py){COLORS.REDL}")
            else:
                print()
                ip = input("  └──> Введите IP адрес : ")

                show_banner(clear=True)

                shodan_host(ip)
                censys_ip(ip)

        elif choice == 2:
            from plugins.domain import domain

            host = input(" └──> Введите хостинг либо IP адрес : ")
            port = ""

            while True:
                try:
                    print()
                    port = input(" └──> Нажмите enter, или напишите свой варианта порта : ")
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
            try:
                domain(host, port)
            finally:
                show_banner(clear=True)

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
            dnsmap_inp = input("    └──> Введите url : ")

            show_banner(clear=True)
            dnsmap(dnsmap_inp)

        elif choice == 5:
            from plugins.metadata import gps_analyzer

            print("\n   Пример пути: /home/bafomet/Desktop/deanon.png\n")
            img_path = input(" └──> Укажите путь до фотографии :")

            show_banner(clear=True)

            gps_analyzer(img_path)

        elif choice == 6:
            from plugins.reverseimagesearch import reverseimagesearch

            print("\n  Пример пути: /home/bafomet/Desktop/deanon.png\n")
            img = input(" └──> Укажите путь до фотографии :")

            show_banner(clear=True)

            reverseimagesearch(img)

        elif choice == 7:
            from plugins.shodan_io import check_shodan_api
            from plugins.honeypot import honeypot

            if not check_shodan_api():
                show_banner(clear=True)
                print(f"{COLORS.REDL}`shodan_api` не валиден, поправь в settings.py токен!{COLORS.REDL}")
            else:
                print()
                hp_inp = input(" └──> Введите IP адрес : ")

                show_banner(clear=True)

                honeypot(hp_inp)

        elif choice == 8:
            from plugins.macaddress import MacAddressLookup

            print()
            mac = input(" └──> Ожидаю ввод MAC адреса :")

            show_banner(clear=True)

            MacAddressLookup(mac)

        elif choice == 9:
            from module.gui import run_gui

            run_gui()

            show_banner(clear=True)

        elif choice == 10:
            from plugins.torrent import torrent
            
            ip_ = input(" └──> Введите IP адрес :")

            show_banner(clear=True)

            torrent(ip_)

        elif choice == 11:
            from module.instagram_search import search_through_instagram

            search_through_instagram()
            show_banner(clear=True)

        elif choice == 12:
            from module.subzone import subzone
            subzone()
            show_banner(clear=True)

        elif choice == 13:
            while 1:
                print("")
                print(" Пример :google.com")
                print("")
                web = prompt(" └──> Введи домен организации :")
                show_banner(clear=True)
                break
            maildb(web)
            continue
                
        elif choice == 14:
            from module import startadb
            startadb.main()
            show_banner(clear=True)

        elif choice == 15:
            while 1:
                os.system("cd plugins/Brother;sudo python3 dlc.py -t manual -k start")
                show_banner(clear=True)
                break
                continue

        elif choice == 16:
            subprocess.call("cd module;python3 hynder.py", shell=True)
            show_banner(clear=True)

        elif choice == 17:
            subprocess.call("sudo etherape", shell=True)
            show_banner(clear=True)

        elif choice == 18:
            os.system("cd core;mpg123 01.mp3")
            show_banner(clear=True)

        elif choice == 19:
            os.system("cd plugins/Brother;sudo python3 dlc2.py -t manual -k start")
            show_banner(clear=True)

        elif choice == 20:
            urls = [
                "https://search4faces.com",
                "https://findclone.ru",
                "https://images.google.com",
                "https://yandex.ru/images",
                "https://tineye.com",
                "https://pimeyes.com/en",
                "https://carnet.ai",
            ]
            for url in urls:
                webbrowser.open(url)

            show_banner(clear=True)

        elif choice == 21:
            from module.Information_services import information_menu
            information_menu()
            show_banner(clear=True)

        elif choice == 22:
            webbrowser.open("https://canarytokens.org")
            show_banner(clear=True)

        elif choice == 23:
            urls = [
                "https://temp-mail.org/ru",
                "https://10minemail.com/ru",
                "https://10minutemail.net/?lang=ru",
                "https://www.lite14.us/10minutemail/russian.html",
                "https://protonmail.com/ru",
                "https://tutanota.com/ru/blog/posts/anonymous-email",
            ]
            for url in urls:
                webbrowser.open(url)

            show_banner(clear=True)

        elif choice == 24:
            from module.password_menu import password_menu
            password_menu()
            show_banner(clear=True)

        elif choice == 25:
            os.system("cd plugins/xss;python2 xss.py")

        elif choice == 26:
            from module.bx54 import bx_menu
            bx_menu()
            show_banner(clear=True)

        elif choice == 27:
            os.system("git clone https://github.com/Bafomet666/osint-info")
            show_banner(clear=True)

        elif choice == 28:
            subprocess.call("sudo maltego", shell=True)
            show_banner(clear=True)

        elif choice == 29:
            while 1:
                os.system("cd module;python3 zoom.py")
                show_banner(clear=True)
                break
                continue

        elif choice == 30:
            from module.deanon_main import deanon_menu

            deanon_menu()
            show_banner(clear=True)

        elif choice == 31:
            webbrowser.open("https://canarytokens.org")
            show_banner(clear=True)

        elif choice == 32:
            pass

        elif choice == 33:
            from module.whoyous import whois_menu

            whois_menu()
            show_banner(clear=True)

        elif choice == 34:
            pass

        elif choice == 35:
            pass

        elif choice == 36:
            pass

        elif choice == 37:
            pass

        elif choice == 38:
            pass

        elif choice == 39:
            pass

        elif choice == 40:
            pass

        elif choice == 41:
            pass
            
        elif choice == 42:
            pass
                    
        elif choice == 43:
            pass

        elif choice == 65:
            webbrowser.open("https://t.me/satana666mx")
            show_banner(clear=True)

        elif choice == 45:
            pass

        elif choice == 75:
            show_banner(clear=True)

        elif choice == 99:
            os.system("python3 osintsan.py")
            return

        elif choice == 88:
            from core.repl_huepl import main

            main()
            show_banner(clear=True)

        elif choice == 0:
            return

        else:
            os.system("clear")
            print(f"{COLORS.REDL}  Опции такой нет, дурак!{COLORS.ENDL}")


if __name__ == '__main__':
    try:
        repl()
    except KeyboardInterrupt:
        os.system("clear")
