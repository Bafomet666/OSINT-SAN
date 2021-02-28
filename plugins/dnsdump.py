#Developer by Bafomet
# -*- coding: utf-8 -*-
import os
import requests
import platform


def dnsmap(domain):

    image = requests.get(f'https://dnsdumpster.com/static/map/{domain}.png')

    if image.status_code == 200:
        image_name = domain.replace(".com", ".ru")
        image_filename = image_name + ".png"
        with open(image_filename, 'wb') as f:
            f.write(image.content)
            print(f"\n{image_filename} DNS Map. Изображение сохраненнo в текущем каталоге ")

            if platform.system() != "Windows":
                pass
            else:
                os.startfile(image_filename)
    else:
        print("Извините, мы не нашли dnsmap")
