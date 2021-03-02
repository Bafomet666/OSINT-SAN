import os
#####  API ТОКЕНЫ, ВПИСЫВАТЬ ВМЕСТО `NONE`
#####  ПО ТИПУ `shodan_api = "..."`
shodan_api = "17x0y"  # https://www.shodan.io
ipstack_api = "278321a02"  # https://ipstack.com
gmap_api = None  # https://developers.google.com/maps/documentation / для gui и для plugins/ipaddress.py
torrent_api = "3cd6463b477d46b79e9eeec21342e4c7"  # https://iknowwhatyoudownload.com/en/api/

# https://developers.virustotal.com/reference#getting-started 
virustotal_api = "353646353565854f53" #Рабочий API plugins/webosint/subdomain.py

cms_detect_api = None  # https://whatcms.org/API  /plugins/webosint/CMSdetect
maildb_api = "e96ed36e3cf64a17c"  # https://api.hunter.io   /plugins/mail.db
zoomeye_api = "eyJh0PQ"  # https://api.zoomeye.org/user/login non required

# (несколько ключей писать через запятую) "API1,API2,API2"
phone_apis = "bcceaaee97"  # https://numverify.com

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PLUGINS_PATH = os.path.join(PROJECT_PATH, 'plugins')
MODULES_PATH = os.path.join(PROJECT_PATH, 'module')
