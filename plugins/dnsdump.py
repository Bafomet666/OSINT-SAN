#Developer by Bafomet
# -*- coding: utf-8 -*-
import re
import os
import requests
import platform


def dnsmap(dnsmap_inp):
    domain = dnsmap_inp

    image = requests.get('https://dnsdumpster.com/static/map/%s.png' % domain)

    if image.status_code == 200:
        image_name = domain.replace(".com",".ru")
        with open('%s.png' % image_name, 'wb') as f:
            f.write(image.content)
            print("\n%s.png DNS Map. Изображение сохраненнo в текущем каталоге " % image_name)

            if (platform.system() != "Windows"):
                pass
            else:
                os.startfile('%s.png' % image_name)
    else:
        print("Извините, мы не нашли dnsmap")
