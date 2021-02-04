#Developer by Bafomet
# -*- coding: utf-8 -*-
import sys
from requests import get
from core.config import shodan_api
#color
R = "\033[31m"   # Red
G = "\033[1;34m" # Blue
C = "\033[1;32m" # Green
W = "\033[0m"    # white
O = "\033[45m"   # Purple

def honeypot(inp):
    honey = "https://api.shodan.io/labs/honeyscore/%s?key=%s" % (inp, shodan_api)
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write("\n%s Нет доступной информации " % bad + "\n")
    if "error" in result or "404" in result:
        print("IP не найден")
        return
    elif result:
            probability = str(float(result) * 10)
            print(G + " [ + ]" + R + " Вероятность что это Honeypot : %s%%" % (probability) + "\n")
            print(G + "  На Shodan проверил, там тоже пусто.")
    else:
        print(" Что-то пошло не так ")
