# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from module.utils.banner import show_banner
from module.utils import COLORS
from osintsan import menu
from osintsan import main1
from plugins.maildb import maildb
from plugins.macaddress import MacAddressLookup
from prompt_toolkit import prompt
from module.Update import update

import subprocess
import os
import webbrowser
import time as t
from grab import Grab


page_8 =f''' {COLORS.GNSL}
  ⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀                         _       _                                           
  ⠀⠀⠀⡏⢢⡁⠂⠤⣀⣀⣀⣀⣀ ⠤⠐⢈⡔⢹                  ___  ___(_)_ __ | |_      ___  __ _ _ __                     
  ⠀⠀⠀⢿⡀⠙⠆⠀⠉⠀⠀⠀⠀⠉⠀⠰⠋⢀⡿                 / _ \/ __| | '_ \| __|____/ __|/ _` | '_ \                    
⠀ ⠀⠀⠀⠈⢷⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡾⠁                | (_) \__ \ | | | | ||_____\__ \ (_| | | | |                   
⠀ ⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹                  \___/|___/_|_| |_|\__|    |___/\__,_|_| |_|                   
  ⣰⠊⠉⠉⠉⡇⠀⠢⣤⣄⠀⠀ ⣠⣤⠔⠀⢸
  ⠙⠓⠒⢦⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎                                     _                                     _ 
  ⠀⠀⠀⠀⡇⠀⠀⠏⠑⠒⠀⠉⠀⠒⠊⠹                 _ __  _   _ _ __ ___ | |__   ___ _ __   _ __ ___   ___   __| |
  ⡎⠉⢹⠀⠙⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⡏⠉⢱         | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| | '_ ` _ \ / _ \ / _` |
  ⢧⡈⠛⠉⠉⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠉⠉⠋⢁⡼         | | | | |_| | | | | | | |_) |  __/ |    | | | | | | (_) | (_| |
  ⠀⢉⣿⠖⠚⠛⢋⢀⠀⠀⠀⠀⠀⠀⠀⡀⡙⠛⠓⠲⣿⣄          |_| |_|\__,_|_| |_| |_|_.__/ \___|_|    |_| |_| |_|\___/ \__,_|
  ⠀⢸⡇⠀⠀⠀⡞⠁⠈⡃⠀⠀⠀⠀⢘⠁⠈⢳⠀⠀⠀⢸⡇
  ⠀⠈⢷⣄⠀⠀⠙⠦⠌⠑⠢⠤⠔⠊⠁⢠⠎⠀⠀⣠⡾⠁
⠀  ⠀⠀⠈⠛⠲⠤⣤⣀⣀⣀⣀⣠⣤⣚⣡⠤⠖⠛⠁

  {COLORS.REDL}[ {COLORS.GNSL}1 {COLORS.REDL}] {COLORS.WHSL} Международный поиск, базовый

  {COLORS.REDL}[ {COLORS.GNSL}2 {COLORS.REDL}] {COLORS.WHSL} Страны бывшего советского союза.
  
  {COLORS.REDL}[ {COLORS.GNSL}99 {COLORS.REDL}] {COLORS.WHSL}В главное меню OSINT-SAN 
 {COLORS.REDL} _________________________________________________________________________________________________________
'''

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

            host = input(" └──> Введите доменное имя : ")
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
            os.system('clear')
            print(page_8)
            option = input(f" {COLORS.REDL} └──> {COLORS.WHSL} Выберите вариант запуска: {COLORS.GNSL}")
            if option == "1":
              from plugins.Phonenumber import phone_number, check_phone_api_token
              if not check_phone_api_token():
                  print(f"{COLORS.REDL}phone api невалиден! (settings.py){COLORS.REDL}")
              else:
                  ph = input(f"\n{COLORS.REDL}  └──>{COLORS.GNSL}  Введи номер телефона с +7: {COLORS.WHSL}")
                  show_banner(clear=True)
                  phone_number(ph)

            elif option == "2":
                g = Grab()
                print(f'\n  {COLORS.WHSL}Пример: {COLORS.GNSL}9262063265\n')
                number = input(f"  {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}] {COLORS.WHSL}Введите номер телефона, без кода страны:{COLORS.GNSL} ")
                g.go('http://phoneradar.ru/phone/' + number)
                try:
                    operator = g.doc.select('//*[@class="table"]/tbody/tr[1]/td[2]').text()
                    region = g.doc.select('//*[@class="table"]/tbody/tr[2]/td[2]').text()
                    sity = g.doc.select('//*[@class="table"]/tbody/tr[3]/td[2]/a').text()
                    search_number = g.doc.select('//*[@class="table"]/tbody/tr[4]/td[2]').text()
                    views_number = g.doc.select('//*[@class="table"]/tbody/tr[5]/td[2]').text()
                    positive_reviews = g.doc.select('//*[@class="table"]/tbody/tr[6]/td[2]').text()
                    negative_reviews = g.doc.select('//*[@class="table"]/tbody/tr[7]/td[2]').text()
                    neutral_reviews = g.doc.select('//*[@class="table"]/tbody/tr[8]/td[2]').text()

                    print(f"\n{COLORS.REDL} Базовые данные о номере:\n")
                    print(f" {COLORS.WHSL}Оператор            :{COLORS.GNSL} {operator}")
                    print(f" {COLORS.WHSL}Регион              :{COLORS.GNSL} {region}")
                    print(f" {COLORS.WHSL}Город               :{COLORS.GNSL} {sity}")
                    print(f" {COLORS.WHSL}Поисков номера      :{COLORS.GNSL} {search_number}")
                    print(f" {COLORS.WHSL}Просмотров номера   :{COLORS.GNSL} {views_number}")
                    print(f" {COLORS.WHSL}Положительные отзывы:{COLORS.GNSL} {positive_reviews}")
                    print(f" {COLORS.WHSL}Отрицательные отзывы:{COLORS.GNSL} {negative_reviews}")
                    print(f" {COLORS.WHSL}Нейтральные отзывы  :{COLORS.GNSL} {neutral_reviews}")
                    print(f" \n{COLORS.WHSL} Обязательно оставляйте отзывы о номере")
                    print(f' {COLORS.WHSL}Нам важен каждый отзыв )')
                    print(f" \n{COLORS.REDL} Комментарии к номеру\n")
                    try:
                        for elem in g.doc.select('//*[@class="card-body"]/div[3]/div'):
                            review = elem.select('div[2]').text()
                            print(f'\n {COLORS.GNSL}[{review}]{COLORS.WHSL}')
                            print(f' {COLORS.REDL}-------------------------------------------------------------------------') 
                            
                    except:
                        print(f" {COLORS.WHSL}Отзывов не найдено")
                except:
                    print(f' {COLORS.WHSL}Информация не найдена')

                print(f'\n{COLORS.WHSL} Второй уровень комментариев:')
                print(f' {COLORS.REDL}-------------------------------------------------------------------------') 
                g.go(f'https://po-nomeru.ru/phone/{number}/')
                try:
                    for elem in g.doc.select('//*[@class="row"]/blockquote'):
                        print(1)
                        avtor_review = elem.select('h3').text()
                        review = elem.select('p').text()
                        print(f' \n{COLORS.GNSL} [{avtor_review}: {review}]\n')
                        print(f' {COLORS.REDL}-------------------------------------------------------------------------{COLORS.WHSL}') 
                    if not avtor_review:
                        print(f" {COLORS.WHSL}Отзывов не найдено\n")
                except:
                    print(f"Нет отзывов!\n")
                print(f' \n Вы желаете оставить отзыв о номере ?\n')
                print(f' {COLORS.REDL}[ {COLORS.GNSL}1 {COLORS.REDL}] - {COLORS.WHSL}Да       {COLORS.REDL}[ {COLORS.GNSL}2 {COLORS.REDL}] -{COLORS.WHSL} Нет\n')
                zapros = input(f' {COLORS.WHSL}\n Введите опцию: {COLORS.GNSL}')
                print('')
                if zapros == '1':
                    show_banner(clear=True)
                    print(f' {COLORS.REDL}-------------------------------------------------------------------------') 
                    print(f' {COLORS.WHSL}Используйте любое имя, отзыв будет оставлен анонимно')
                    print(f' {COLORS.WHSL}Но я бы на вашем месте не отказался от proxy/vpn')
                    name = input(f'\n {COLORS.WHSL}Введите ваше имя: {COLORS.GNSL}')
                    message = input(f'\n {COLORS.WHSL}Введите ваш отзыв о владельце номера:{COLORS.GNSL} ')
                    rating = input(f'\n {COLORS.GNSL}Выберите рейтинг человека:\n'
                    
                      f'{COLORS.REDL} [ {COLORS.GNSL}1 {COLORS.REDL}] -{COLORS.WHSL} Положительный, можно звонить и отвечать на звонок.\n'
                      f'{COLORS.REDL} [ {COLORS.GNSL}2 {COLORS.REDL}] -{COLORS.WHSL} Отрицательный, не отвечать на звонок с этого номера.\n'
                      f'{COLORS.REDL} [ {COLORS.GNSL}3 {COLORS.REDL}] -{COLORS.WHSL} Нейтральный.\n Введите рейтинг: ')
                    g.setup(headers={'X-Requested-With': 'XMLHttpRequest',
                                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                        'Origin': 'https://po-nomeru.ru'})
                    g.setup(post={'name': name,
                                    'message': message,
                                    'rating': rating,
                                    'number': number,
                                    'action': 'addReview'})
                    g.go('https://po-nomeru.ru/comments/')
                    print(f' \n{COLORS.REDL}Поздравляю !!! Ваш отзыв добавлен. ')
                else:
                    pass
                    show_banner(clear=True)
                    

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
            while 1:
                show_banner(clear=True)
                print("")
                mac = prompt(" └──> Введите mac address: ") 
                break
            MacAddressLookup(mac)
            continue

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
            os.system("cd plugins/Brother;python3 dlc.py -t manual -k start")
            show_banner(clear=True)

        elif choice == 16:
            subprocess.call("cd module;python3 shodan_module.py", shell=True)
            show_banner(clear=True)

        elif choice == 17:
            subprocess.call("sudo etherape", shell=True)
            show_banner(clear=True)

        elif choice == 18:
            print()
            print("   Проверка всех модулей")
            t.sleep(6)
            print("   \nРаботает в штатном режиме")
            t.sleep(2)
            show_banner(clear=True)

        elif choice == 19:
            # Это дополнительный модуль
            show_banner(clear=True)
            os.system("cd module/maigret;python3 wizard.py")

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
                   
        elif choice == 55:
            while 1:
                break
            update()
            continue

        elif choice == 65:
            webbrowser.open("https://t.me/satana666mx")
            show_banner(clear=True)
            
        elif choice == 75:
            main1()

        elif choice == 99:
            show_banner(clear=True)

        elif choice == 88:
            from core.repl_huepl import main

            main()
            show_banner(clear=True)

        elif choice == 00:
            return

        else:
            exit()
            os.system("clear")
            print(f"{COLORS.REDL}  Опции такой нет, дурак!{COLORS.ENDL}")


if __name__ == '__main__':
    try:
        repl()
    except KeyboardInterrupt:
        os.system("clear")
