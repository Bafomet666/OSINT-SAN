#Developer by Bafomet
# -*- coding: utf-8 -*-
import sys
from requests import get
from core.config import shodan_api


def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=%s' % (inp, shodan_api)
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write('\n%s Нет доступной информации ' % bad + '\n')
    if "error" in result or "404" in result:
        print("IP Not found")
        return
    elif result:
            probability = str(float(result) * 10)
            print('\n[ + ] Вероятность что это Honeypot : %s%%' % (probability) + '\n')
    else:
        print(" Что-то пошло не так ")
