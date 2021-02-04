# -*- coding: utf8 -*-
#Developer by Bafomet
import json
from requests import get
#color
R = '\033[31m'   # Red
G = '\033[1;34m' # Blue
C = '\033[1;32m' # Green
W = '\033[0m'    # white
O = '\033[45m'   # Purple

def censys_ip(IP):
    try:
        dirty_response = get('https://censys.io/ipv4/%s/raw' % IP).text
        clean_response = dirty_response.replace('&#34;', '"')
        x = clean_response.split('<code class="json">')[1].split('</code>')[0]
        censys = json.loads(x)
        
        print("")
        print(R + " [ + ]" + C + " Получена информация с Censys. " + C + "\n")
        print(G + " [ + ]" + C + " Страна -------> "+str(censys["location"]["country"]))
        print(G + " [ + ]" + C + " Континент-----> "+str(censys["location"]["continent"]))
        print(G + " [ + ]" + C + " Код страны -- > "+str(censys["location"]["country_code"]))
        print(G + " [ + ]" + C + " Широта  ------> "+str(censys["location"]["latitude"]))
        print(G + " [ + ]" + C + " Долгота  -----> "+str(censys["location"]["longitude"]))
    except:
        print(G + " [ + ]" + R + " Чет я нехуя нечего не нашел")
