#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
from utils import COLORS
import random
import shodan
import time
import sys
import os

page_8 =f'''
   ______    ______   ______  __    __  ________        ______    ______   __    __         ______   __                        __                     
  /      \  /      \ /      |/  \  /  |/        |      /      \  /      \ /  \  /  |       /      \ /  |                      /  |                    
 /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \ $$ |$$$$$$$$/      /$$$$$$  |/$$$$$$  |$$  \ $$ |      /$$$$$$  |$$ |____    ______    ____$$ |  ______   _______  
 $$ |  $$ |$$ \__$$/   $$ |  $$$  \$$ |   $$ | ______ $$ \__$$/ $$ |__$$ |$$$  \$$ |      $$ \__$$/ $$      \  /      \  /    $$ | /      \ /       \ 
 $$ |  $$ |$$      \   $$ |  $$$$  $$ |   $$ |/      |$$      \ $$    $$ |$$$$  $$ |      $$      \ $$$$$$$  |/$$$$$$  |/$$$$$$$ | $$$$$$  |$$$$$$$  |
 $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |$$$$$$/  $$$$$$  |$$$$$$$$ |$$ $$ $$ |       $$$$$$  |$$ |  $$ |$$ |  $$ |$$ |  $$ | /    $$ |$$ |  $$ |
 $$ \__$$ |/  \__$$ | _$$ |_ $$ |$$$$ |   $$ |        /  \__$$ |$$ |  $$ |$$ |$$$$ |      /  \__$$ |$$ |  $$ |$$ \__$$ |$$ \__$$ |/$$$$$$$ |$$ |  $$ |
 $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |        $$    $$/ $$ |  $$ |$$ | $$$ |      $$    $$/ $$ |  $$ |$$    $$/ $$    $$ |$$    $$ |$$ |  $$ |
  $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/          $$$$$$/  $$/   $$/ $$/   $$/        $$$$$$/  $$/   $$/  $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/ 

                                                        
'''
os.system('clear')
print(page_8)
print(f' {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL} Обязательно cделай сохранение информации\n')
data = input(f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL} Выполнить сохранение результата в файле? y/n:{COLORS.WHSL} ").strip()
l0g = ("")

def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(data)
    file.close()

if data.startswith("y" or "Y"):
    l0g = input(f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL} Дайте название файлу:{COLORS.WHSL} ")
    print("")
    print(f" Данные будут сохранены по пути: OSINT-SAN /module/ Название файла")
    print(f"\n" + "  " + "»" * 80 + "\n")
    logger(data)
else:
    print("")
    print (f"{COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL} Внимание: поисковые запросы НЕ БУДУТ СОХРАНЕНЫ !!! \n")

def showdam():
    if os.path.exists("./api_shodan.txt") and os.path.getsize("./api_shodan.txt") > 0:
        with open("api_shodan.txt", "r") as file:
            shodan_api_key = file.readline().rstrip("\n")
    else:
        file = open("api_shodan.txt", "w")
        os.system("stty -echo")
        shodan_api_key = input(f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}Ваш ключ не валидный. Введите другой: ")
        os.system("stty echo")
        file.write(shodan_api_key)
        print(f"\n Проверка API модуля ")
        file.close()

    api = shodan.Shodan(shodan_api_key)
    time.sleep(0.4)

    limit = 200  # Здесь вы можете изменять лимит запросов
    counter = 1

    try:
        print(f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL} Проверка вашего ключа\n")
        api.search("b00m")
        print(f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.WHSL} Авторизация успешно пройдена\n")
        time.sleep(0.5)
        b00m = input(f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL} Введите ключевой запрос поиска:{COLORS.WHSL} ")
        print("")
        counter = counter + 1
        for banner in api.search_cursor(b00m):
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  IP address  :{COLORS.WHSL}  " + (banner["ip_str"]))
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Порт        :{COLORS.WHSL}  " + str(banner["port"]))
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Организация :{COLORS.WHSL}  " + str(banner["org"]))
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Геолокация  :{COLORS.WHSL}  " + str(banner["location"]))
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Layer       :{COLORS.WHSL}  "+ (banner["transport"]))
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Domains     :{COLORS.WHSL}  " + str(banner["domains"]))
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Hostnames   :{COLORS.WHSL}  " + str(banner["hostnames"]))
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  № Результата:{COLORS.WHSL}  %s. Search query: %s" % (str(counter), str(b00m)))

            data = ("\nIP: " + banner["ip_str"]) + ("\nPort: " + str(banner["port"])) + ("\nOrganisation: " + str(banner["org"])) + ("\nLocation: " + str(banner["location"])) + ("\nLayer: " + banner["transport"]) + ("\nDomains: " + str(banner["domains"])) + ("\nHostnames: " + str(banner["hostnames"])) + ("\nData\n" + banner["data"])
            logger(data)
            time.sleep(0.1)
            print ("\n" + "  " + "»" * 78 + "\n")

            counter += 1
            if counter >= limit:
                print(f'       {COLORS.REDL}                        !!!  ВНИМАНИЕ  !!!\n')
                print(f'  У вас есть 10 секунд на прочтение сообщения')
                print(f'  Данные успешно собраны, сейчас мы вас переместим в меню, все данные сохранены в папке module')
                time.sleep(12)
                exit()

    except KeyboardInterrupt:
            print("\n")
            print(" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL} Выполняем обратный переход.")
            time.sleep(0.5)

    except shodan.APIError as oeps:
            print (f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Суточные лимиты ключа привышены, попробуйте завтра %s " % (oeps))
            sha_api = input(f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Хотите поменять API-ключ ? | Y да / N нет, выход:  ").lower()
            if sha_api.startswith("y" or "Y"):
                file = open("api_shodan.txt", "w")
                os.system("stty -echo")
                shodan_api_key = input(  " [ + ]  Ваш ключ не рабочий. ")
                os.system("stty echo")
                file.write(shodan_api_key)
                print(f"\n Проверка API модуля")
                file.close()
                print(f" {COLORS.REDL}[ {COLORS.GNSL}+ {COLORS.REDL}]{COLORS.GNSL}  Перезапуск, подождите. ")
                time.sleep(1)
                showdam()
            else:
                print ("")
                sys.exit()

# =====# Main #===== #
#bafomet
if __name__ == "__main__":
    showdam()
