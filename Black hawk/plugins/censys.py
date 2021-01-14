# -*- coding: utf8 -*-
#Developer by Bafomet
import json
from requests import get

def censys_ip(IP):
    try:
        dirty_response = get('https://censys.io/ipv4/%s/raw' % IP).text
        clean_response = dirty_response.replace('&#34;', '"')
        x = clean_response.split('<code class="json">')[1].split('</code>')[0]
        censys = json.loads(x)

        print("\n[ + ] Собираем информацию с Сensys \n")
        print("[ + ] Страна -------> "+str(censys["location"]["country"]))
        print("[ + ] Континент-----> "+str(censys["location"]["continent"]))
        print("[ + ] Код страны -- > "+str(censys["location"]["country_code"]))
        print("[ + ] Широта  ------> "+str(censys["location"]["latitude"]))
        print("[ + ] Долгота  -----> "+str(censys["location"]["longitude"]))
    except:
        print("Unavailable")
