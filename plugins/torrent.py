# -*- coding: utf8 -*-
#Developer by Bafomet
from settings import torrent_api

import requests
#color
R = '\033[31m'   # Red
G = '\033[1;34m' # Blue
C = '\033[1;32m' # Green
W = '\033[0m'    # white
O = '\033[45m'   # Purple


def torrent(IP):
    r = requests.get(
        "https://api.antitor.com/history/peer/",
        params={"ip": IP, "key": torrent_api},
    )
    res = r.json()
    print(f"{R} [ + ]{C} Найдена информация по загрузкам Torrent." + "\n")

    if len(res) > 4:
        print(f"  IP Address: {res['ip']}")
        print(f"  ISP: {res['isp']}")

        geo_data = res['geoData']
        print(f"  Country: {geo_data['country']}")
        print(f"  Latitude: {geo_data['latitude']}")
        print(f"  Longitude: {geo_data['longitude']}")
        print()

        for i in res["contents"]:
            print(f"  Category:{i['category']}")
            print(f"  Name:{i['name']}")
            print(f"  Start:{i['startDate']}")
            print(f"  End:{i['endDate']}")
            print(f"  Size:{i['torrent']['size']}")
            print()
    else:
        print(f"{G} [ + ]{R} Чет я нехуя нечего не нашел")
