import os
# API ТОКЕНЫ, Записывать внутри "  "
# ПО ТИПУ `shodan_api = "..."`
shodan_api = "  "  # https://www.shodan.io
ipstack_api = "  "  # https://ipstack.com
gmap_api = "  "  # https://developers.google.com/maps/documentation / для gui и для plugins/ipaddress.py
torrent_api = "  "  # https://iknowwhatyoudownload.com/en/api/

# https://developers.virustotal.com/reference#getting-started 
virustotal_api = "  " #Рабочий API plugins/webosint/subdomain.py

cms_detect_api = "  "  # https://whatcms.org/API  /plugins/webosint/CMSdetect
maildb_api = "  "  # https://api.hunter.io   /plugins/mail.db
zoomeye_api = "  "  # https://api.zoomeye.org/user/login non required

# (несколько ключей писать через запятую) "API1,API2,API2"
phone_apis = "  "  # https://numverify.com

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PLUGINS_PATH = os.path.join(PROJECT_PATH, 'plugins')
MODULES_PATH = os.path.join(PROJECT_PATH, 'module')


# Зайди еще в папку plugins открой там maildb.py и впиши еще один API c hunter.io
