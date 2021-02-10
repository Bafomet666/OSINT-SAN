#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
#и одного импорта хватит с головой
from settings import maildb_api

import requests

# Set color
R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
P = '\033[1;35m' # Purple


def check_maildb_token():
    return not maildb_api


def maildb(emailaddress):
    if "@" in emailaddress and (".com" in emailaddress or ".in" in emailaddress):

        url = "https://api.hunter.io/v2/domain-search"
        response = requests.get(
            url,
            params={
                "domain": emailaddress,
                "api_key": maildb_api,
            },
        )

        result = response.json()
        print(f"{R} [ + ] {G}Собрано из домена {emailaddress}")
        print()

        emails = result['data']['emails']
        for email in emails:
            print(f"  Email ID   :{email['value']}")
            print(f"  First Name :{email['first_name']}")
            print(f"  Last Name  :{email['last_name']}")

            if email['position']:
                print(f"  Position   :{email['position']}")
            if email['linkedin']:
                print(f"  Linkedin   :{email['linkedin']}")
            if email['twitter']:
                print(f"   Twitter    :{email['twitter']}")
            print()

    else:
        print(f"{R} Такого домена не существует хули ты мне пиздишь")
