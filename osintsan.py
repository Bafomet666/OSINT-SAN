# Студия разработки Bafomёd group
# Получить доступ можно у https://t.me/satana666mx
# Официальный канал https://t.me/osint_san_framework
# Наш сайт: https://osintsan.ru/
import os
from core.core import osint
from module.utils.licensysi import licence, check_licence

# Вам необходимо использовать свои API для максимальной анонимности и защиты переваемых данных.

api = {
    "Shodan": " здесь_писать_апи ",
    # Ваш личный token Shodan, вписывать между "сюда_вписывать_ваш_токен"  Получать токен в -->> https://www.shodan.io/

    "Gmap_g": " здесь_писать_апи ",
    # Ваш личный token google, вписывать между "сюда_вписывать_ваш_токен" Получать токен в -->>
    # https://console.cloud.google.com/google/maps-apis/

    "IP_api": " здесь_писать_апи ",  # API Массового сканирование ip address "сюда_вписывать_ваш_токен"
    # Получать токен в -->> https://ipapi.com/

    "ngrok.set_auth_token": " здесь_писать_апи ",
    # big brother 13,  "сюда_вписывать_ваш_токен" # Получать токен в -->>
    # https://dashboard.ngrok.com/get-started/your-authtoken

    "virustotal_api": " ",
    # Выше впиши API вирус тотал
    "cms_detect_api": "здесь_писать_апи",

    "phone_apis": " здесь_писать_апи ", # API номер телефона phone_apis -- https://numverify.com/dashboard?logged_in=1

}

LICENCE_FILENAME = 'licence.json'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_LICENCE = os.path.join(BASE_DIR, LICENCE_FILENAME)


def osintsan():
    os.system('clear')
    print('\n Друг, надеюсь ты указал API в api.py')
    osint()


if __name__ == '__main__':
    if not check_licence(PATH_TO_LICENCE):
        licence(PATH_TO_LICENCE)

    osintsan()


