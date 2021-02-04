# -*- coding: utf8 -*-
#Developer by Bafomet
import requests
#color
R = '\033[31m'   # Red
G = '\033[1;34m' # Blue
C = '\033[1;32m' # Green
W = '\033[0m'    # white
O = '\033[45m'   # Purple

def torrent(IP):

    r = requests.get("https://api.antitor.com/history/peer/?ip="+ IP +"&key=3cd6463b477d46b79e9eeec21342e4c7")
    res = r.json()
    print (R + " [ + ]" + C + " Найдена информация по загрузкам Torrent." + "\n")
    if len(res)>4:
        print("  IP Address: "+res["ip"])
        print("  ISP: "+res["isp"])
        print("  Country: "+res["geoData"]["country"])
        print("  Latitude: "+str(res["geoData"]["latitude"]))
        print("  Longitude: "+str(res["geoData"]["longitude"])+"\n")
        for i in res["contents"]:
        	print("  Category:"+i["category"])
        	print("  Name:"+i["name"])
        	print("  Start:" + i["startDate"])
        	print("  End:" + i["endDate"])
        	print("  Size:"+str(i["torrent"]["size"]))
        	print("")
    else:
        print(G + " [ + ]" + R + " Чет я нехуя нечего не нашел")
