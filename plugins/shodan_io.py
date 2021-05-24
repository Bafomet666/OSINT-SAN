#Developer by Bafomet
# -*- coding: utf-8 -*-
import shodan
from settings import shodan_api

api = shodan.Shodan(shodan_api)


def check_shodan_api():
    if not shodan_api:
        return False

    try:
        api.info()
    except shodan.APIError:
        return False

    return True


#color
R = "\033[31m"   # Red
G = "\033[1;34m" # Blue
C = "\033[1;32m" # Green
W = "\033[0m"    # white
O = "\033[45m"   # Purple


def shodan_host(IP):
    try:
        host = api.host(IP)
        print(R + " [ + ]" + C + " Мы собираем информацию: " + C + "\n")
        print(R + " [ + ]" + C + " Получена информация с Shodan. \n")
        print(G + " [ + ]" + C + " IP Address ----> " + str(host["ip_str"]))
        print(G + " [ + ]" + C + " Страна  -------> " + str(host["country_name"]))
        print(G + " [ + ]" + C + " Город----------> " + str(host["city"]))
        print(G + " [ + ]" + C + " Организация  --> " + str(host["org"]))
        print(G + " [ + ]" + C + " ISP -----------> " + str(host["isp"]))
        print(G + " [ + ]" + C + " Открытые порты > " + str(host["ports"]))
    except:
        print(G + " [ + ]" + R + " Был я щас на Shodan и Censys, там пусто, ты или хуйню ввел, или напиздеть мне пытаешься")
        print("")
        print(G + " [ + ]" + R + " Не еби мое кибер ядро, введи нормально IP адрес, ламер ебаный")
        print("")


def shodan_ip(IP):
    try:
        host = api.host(IP)
        print(R + " [ + ]" + C + " Поиск и сбор информации с Shodan. " + C + "\n")
        print(G + " [ + ]" + C + " IP Address ----> " + str(host["ip_str"]))
        print(G + " [ + ]" + C + " Страна  -------> " + str(host["country_name"]))
        print(G + " [ + ]" + C + " Город ---------> " + str(host["city"]))
        print(G + " [ + ]" + C + " Организация  --> " + str(host["org"]))
        print(G + " [ + ]" + C + " ISP -----------> " + str(host["isp"]))
        print(G + " [ + ]" + C + " Открытые порты-> " + str(host["ports"]))
    except:
        print(G + " [ + ]" + R + " Чет я нехуя нечего не нашел")
        print("")
