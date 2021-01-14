# -*- coding: utf-8 -*-
import requests

def MacAddressLookup(mac):
    url = ("https://macvendors.co/api/" + mac)
    response=requests.get(url)
    result=response.json()
    if result["result"]:
        final=result['result']
        print("Компания:" + final["company"])
        print("Адрес:" + final["address"])
        print("Страна:" + final["country"])
        print("")
    else:
        print("Error: Something Went Wrong")
