import os
#Регистрируй. Там 2 API я оставил вам подарком.
#####  API ТОКЕНЫ, ВПИСЫВАТЬ ВМЕСТО `NONE`
#####  ПО ТИПУ `shodan_api = "..."`
shodan_api = "17x0y"  # https://www.shodan.io
ipstack_api = "278321a02"  # https://ipstack.com
gmap_api = None  # https://developers.google.com/maps/documentation
torrent_api = "3cd6463b477d46b79e9eeec21342e4c7"  # https://api.antitor.com #Рабочий API

# https://developers.virustotal.com/reference#getting-started 
virustotal_api = "1af37bfeb7b1628ba10695fb187987a6651793e37df006a5cdf8786b0e4f6453" #Рабочий API

cms_detect_api = None  # https://whatcms.org/API
maildb_api = "e96ed36e3cf64a17c"  # https://api.hunter.io
zoomeye_api = "eyJh0PQ"  # https://api.zoomeye.org/user/login non required

# (несколько ключей писать через запятую) "API1,API2,API2"
phone_apis = "bcceaaee97"  # http://apilayer.net/api

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PLUGINS_PATH = os.path.join(PROJECT_PATH, 'plugins')
MODULES_PATH = os.path.join(PROJECT_PATH, 'module')
