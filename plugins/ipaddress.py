from settings import gmap_api, ipstack_api

import requests
import gmplot
# from plugins.api import ipstack
import webbrowser
import re
# from plugins.api import gmap
from ipaddress import *
from plugins.webosint.who.whois import *


if not ipstack_api:
    print("Добавьте ключ api ipstack в settings.py")

if not gmap_api:
    print("Добавьте ключ API Google Heatmap в settings.py")


def IPHeatmap():
    print('''
    1) Trace single IP
    2) Trace multiple IPs''')
    choice = input("OPTIONS >> ")

    if choice == '1':
        IP = input("Enter the IP : ")
        read_single_IP(IP)
    elif choice == '2':
        IP_file = input("Enter the IP File Location : ")
        read_multiple_IP(IP_file)
    else:
        print("\nError: Please choose an appropriate option")


def read_single_IP(IP):
    print ('[ + ]' + " Идет сбор информации : %s ..." %IP + '\n')
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",IP):
        print("Invalid IP Address")
        IPHeatmap()
    lats = []
    lons = []
    r = requests.get(f"http://api.IPstack.com/{IP}", params={"access_key": ipstack_api})
    response = r.json()
    print()
    print(f"[ + ] IP адрес :{response['ip']}")
    print(f"[ + ] Локация : {response['region_name']}")
    print(f"[ + ] Страна : {response['country_name']}")
    print(f"[ + ] Долгота : {response.get('latitude')}")
    print(f"[ + ] Широта : {response.get('longitude')}")
    if input("[ + ] Открыть еще больше информации  (Y/N): ").upper() == "Y":
        whois_more(IP)
    if response.get('latitude') and response.get('longitude'):
        lats = response['latitude']
        lons = response['longitude']
    query = f"{lats},+{lons}"
    maps_url = f"https://maps.google.com/maps?q={query}"
    print()
    openWeb = input(" [ + ] Открыть местоположение GPS в web broser? (Y/N) ")
    if openWeb.upper() == 'Y':
        webbrowser.open(maps_url, new=2)
    else:
        pass


def read_multiple_IP(IP_file):
    lats = []
    lons = []
    try:
        f = open(IP_file, "r")
        f1 = f.readlines()
        print('[ + ]' + " Загрузка информации, сходи пока чай налей. Выпей, расслабься, если более сотни делаешь, долго..." + '\n')
        for line in f1:
            IP=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",line)
            IP=IP.group()
            r = requests.get("http://api.IPstack.com/" + IP + "?access_key=" + ipstack_api)
            response = r.json()
            if response['latitude'] and response['longitude']:
                lats.append(response['latitude'])
                lons.append(response['longitude'])
        heat_map(lats,lons)
    except IOError:
        print("ERROR : Файл не существует\n")
        IPHeatmap()


def heat_map(lats, lons):
    gmap3 = gmplot.GoogleMapPlotter(20.5937, 78.9629, 5)
    gmap3.heatmap(lats, lons)
    gmap3.scatter(lats, lons, '#FF0000', size=50, marker=False)
    gmap3.plot(lats, lons, 'cornflowerblue', edge_width = 3.0)
    save_location = input(" [ + ] Введите место для сохранения файла : ")
    gmap3.apikey = gmap_api
    location = save_location + "/heatmap.html"
    gmap3.draw(location)
    print("[ + ] Heatmap saved at " + location)
    openWeb = input(" [ + ] Открыть в web broser? (Y/N) : ")
    if openWeb.upper() == 'Y':
        webbrowser.open(url=("file:///"+location))
    else:
        pass
