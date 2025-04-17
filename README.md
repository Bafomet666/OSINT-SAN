


#                                                                          OSINT-SAP Project.

![alt tag](https://github.com/Bafomet666/OSINT-SAN/blob/main/report/Screenshot%20at%202024-04-03%2017-29-19.png)

Бесплатный OSINT-SAN Framework дает возможность быстро находить информацию и деанонимизировать пользователей сети интернет. С помощью нашего ПО вы сможете собирать информацию о пользователях как при использовании linux.

Фрэйм адаптирован под: Parrot OS, Kali linux

----

О нас:

Наш сайт: https://osintsan.ru

Telegram: https://t.me/osint_san_framework

----

Если вы используете free версию вам нужно вписать целый ряд API ключей, если вы используете версию PRO вам нужен только один API это zoomeye. Получаем API на сайтах указанных ниже, дальше вписываем все api в osintsan.py


    API для получения информации о номере https://numverify.com

    Shodan API https://www.shodan.io

    Проверка на CMS https://whatcms.org/API

    Ngrok для big brother https://ngrok.com

    Torrent API https://iknowwhatyoudownload.com/en/api/

    VirusTotal бесплатная служба проверки https://developers.virustotal.com/v3.0/reference

Далее установка зависимостей командой

sudo pip3 install -r requirements.txt

Если вдруг у вас не установлен python3 последней версии, обязательно установите его.

     https://linuxize.com/post/how-to-install-python-3-9-on-debian-10/

     sudo apt install -y python3-pip
     
Внимание, мы поменяли путь api с api.py в osintsan.py
     

#### Возникли ошибки при установке зависимостей ? Решение проблем тут: https://github.com/Bafomet666/OSINT-SAN/issues/11
---

### Использование framework:

Запускать бесплатную версию командой: python3 osintsan.py, платную версию python3 san.py

После успешной авторизации, вам будет доступно меню модулей.

---

Приятного использования.

Вы должны использовать этот framework только для законной проверки, согласованной обоими сторонами,
или для образовательных целей, я не несу ответственность за нанесенный вами
Ущерб, вызванный osintsan.





