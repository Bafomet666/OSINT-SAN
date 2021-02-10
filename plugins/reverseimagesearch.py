#-*- coding: utf-8 -*-
#Developer by Bafomet
import requests
import webbrowser


def reverseimagesearch(img):
    upload_url = "https://www.google.co.in/searchbyimage/upload"
    try:
        files = {'encoded_image': (img, open(img, 'rb')), 'image_content': ''}
    except IOError:
        print("\nERROR: Файл не найден!\n")
        return

    response = requests.post(upload_url, files=files, allow_redirects=False)
    fetch_url = response.headers['Location']
    open_web = input(" Я открою браузер ? Мне тебе результаты нужно показать (Y/N) : ")
    if open_web.upper() == 'Y':
        webbrowser.open(fetch_url)
    else:
        pass
