# Студия разработки Bafomёd group
# Получить доступ можно у https://t.me/satana666mx
# Официальный канал https://t.me/osint_san_framework
# Наш сайт: https://osintsan.ru/
import os
from core.core import main, licence, check_licence

# Внимание впишите между '' свои API ниже, пример: shodan = 'ащ34гн49арлмокщ48ущышолдвв'

# Здесь хранится твой ngrok токен (API) -- https://ngrok.com/
token = "Здесь прописать api"

# Ваш личный код Shodan -- https://www.shodan.io/
shodan_api_key = "Здесь прописать api"

# API номер телефона phone_apis -- https://numverify.com/dashboard?logged_in=1
phone_apis = "Здесь прописать api"

# Torrent API  ---  https://iknowwhatyoudownload.com/en/api/
torrent_api = "Здесь прописать api"

# Virus total api -- https://developers.virustotal.com/reference#getting-started 
virustotal_api = "Здесь прописать api"

# Качать здесь https://whatcms.org/
cms_detect_api = "Здесь прописать api"


LICENCE_FILENAME = 'licence.json'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_LICENCE = os.path.join(BASE_DIR, LICENCE_FILENAME)


def osintsan():
    main()


if __name__ == '__main__':
    if not check_licence(PATH_TO_LICENCE):
        licence(PATH_TO_LICENCE)

    osintsan()
