#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
#и одного импорта хватит с головой
import requests

# Set color
R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Purple

def maildb(emailaddress):
    if  ("@" and ".com") or ("@" and ".in") in emailaddress:
        req=requests.get("https://api.hunter.io/v2/domain-search?domain="+emailaddress+"&api_key=e96ed3505243d15c9250455a394376e3cf64a17c")
        j=req.json()
        print(R+" [ + ] "+ G +"Собрано из домена "+emailaddress+"...\n")
        for i in range(len(j['data']['emails'])):
            print("  Email ID   :",j['data']['emails'][i]['value'])
            print("  First Name :",j['data']['emails'][i]['first_name'])
            print("  Last Name  :",j['data']['emails'][i]['last_name'])
            if j['data']['emails'][i]['position']!=None:
                print("  Position   :",j['data']['emails'][i]['position'])
            if j['data']['emails'][i]['linkedin']!=None:
                print("  Linkedin   :",j['data']['emails'][i]['linkedin'])
            if j['data']['emails'][i]['twitter']!=None:
                print("Twitter    :",j['data']['emails'][i]['twitter'])
            print()
    else:
        print(R+" Такого домена не существует хули ты мне пиздишь")
