#Developer by Bafomet
# -*- coding: utf-8 -*-
import shodan
from core.config import shodan_api

api = shodan.Shodan(shodan_api)
#color
R = '\033[31m'   # Red
G = '\033[1;34m' # Blue
C = '\033[1;32m' # Green
W = '\033[0m'    # white
O = '\033[45m'   # Purple

def shodan_host(IP):
    try:
        host = api.host(IP)
        print(R + '[ + ]' + C + ' Мы собираем информацию с Shodan : ' + C + '\n')
        print("\n Результат получен : \n")
        print("[ + ] IP Address ----> " + str(host['ip_str']))
        print("[ + ] Страна  -------> " + str(host['country_name']))
        print("[ + ] Город----------> " + str(host['city']))
        print("[ + ] Организация  --> " + str(host['org']))
        print("[ + ] ISP -----------> " + str(host['isp']))
        print("[ + ] Открытые порты > " + str(host['ports']))
    except:
        print("[ + ] Нечего не найдено")


def shodan_ip(IP):
    try:
        host = api.host(IP)
        print("\n[ + ] Поиск и сбор информации на Shodan \n")
        print("[ + ] IP Address ----> " + str(host['ip_str']))
        print("[ + ] Страна  -------> " + str(host['country_name']))
        print("[ + ] Город ---------> " + str(host['city']))
        print("[ + ] Организация  --> " + str(host['org']))
        print("[ + ] ISP -----------> " + str(host['isp']))
        print("[ + ] Открытые порты-> " + str(host['ports']))
    except:
        print("[ + ] Нечего не найдено")
