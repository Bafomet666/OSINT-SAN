# -*- coding: utf8 -*-
#Developer by Bafomet
from module.utils import COLORS

import json
import requests


def censys_ip(IP):
    try:
        dirty_response = requests.get(f'https://censys.io/ipv4/{IP}/raw').text
        clean_response = dirty_response.replace('&#34;', '"')
        x = clean_response.split('<code class="json">')[1].split('</code>')[0]
        censys = json.loads(x)
        
        print("")
        print(COLORS.R + " [ + ]" + COLORS.C + " Получена информация с Censys. " + COLORS.C + "\n")
        print(COLORS.G + " [ + ]" + COLORS.C + " Страна -------> "+str(censys["location"]["country"]))
        print(COLORS.G + " [ + ]" + COLORS.C + " Континент-----> "+str(censys["location"]["continent"]))
        print(COLORS.G + " [ + ]" + COLORS.C + " Код страны -- > "+str(censys["location"]["country_code"]))
        print(COLORS.G + " [ + ]" + COLORS.C + " Широта  ------> "+str(censys["location"]["latitude"]))
        print(COLORS.G + " [ + ]" + COLORS.C + " Долгота  -----> "+str(censys["location"]["longitude"]))
    except:
        print(COLORS.G + " [ + ]" + COLORS.R + " Чет я нехуя нечего не нашел")
