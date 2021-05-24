#Developer by Bafomet
# -*- coding: utf-8 -*-
import requests
from settings import shodan_api

# color
R = "\033[31m"   # Red
G = "\033[1;34m" # Blue
C = "\033[1;32m" # Green
W = "\033[0m"    # white
O = "\033[45m"   # Purple


def honeypot(inp):
    url = f"https://api.shodan.io/labs/honeyscore/{inp}"

    try:
        result = requests.get(url, params={"key": shodan_api}).text
    except:
        print(f"\nНет доступной информации!")
        return

    if "error" in result or "404" in result:
        print("IP не найден")
        return

    elif result:
        probability = str(float(result) * 10)
        print(f"{G} [ + ]{R} Вероятность что это Honeypot : {probability}%")
        print()
        print(f"{G}  На Shodan проверил, там тоже пусто.")

    else:
        print(" Что-то пошло не так ")
