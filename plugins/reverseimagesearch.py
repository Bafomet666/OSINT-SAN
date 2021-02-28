#-*- coding: utf-8 -*-
#Developer by Bafomet
import json
import os

import requests
import webbrowser


def get_url_results(img):
    google_images_url = "https://images.google.com/searchbyimage/upload"
    google_response = requests.post(
        google_images_url,
        files={'encoded_image': (img, open(img, 'rb')), 'image_content': ''}
    )
    result_google = google_response.history.pop().url

    yandex_images_url = 'https://yandex.ru/images/search'
    response = requests.post(
        yandex_images_url,
        params={
            'rpt': 'imageview',
            'format': 'json',
            'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'
        },
        files={'upfile': ('blob', open(img, 'rb'), 'image/jpeg')},
    )
    data = json.loads(response.content)
    if data.get("type") == "catcha" or not data.get('blocks'):
        print(" Yandex поймал нас на капче, придется ручками...\n")
        result_yandex = yandex_images_url
    else:
        query_string = data['blocks'][0]['params']['url']
        result_yandex = f"{yandex_images_url}?{query_string}"
    return result_google, result_yandex


def reverseimagesearch(img):
    if not os.path.exists(img):
        print("\nERROR: Файл не найден!\n")
        return

    urls = get_url_results(img)

    open_web = input(" Я открою браузер ? Мне тебе результаты нужно показать (Y/N) : ")
    if open_web.upper() == 'Y':
        for url in urls:
            webbrowser.open(url)
    else:
        pass
