#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
# Это больше пcихологическая авторизация чем для защиты кода. Так что нечего не трогай

from core import repl_prompt
from module.utils.preload_banners import BANNER1, BANNER2
from module.utils.banner import show_banner
import getpass
import random

import os
import time


# Set color
R = '\033[31m'    # Red
N = '\033[1;37m'  # White
G = '\033[32m'    # Green
B = '\033[1;34m'  # Blue
P = '\033[1;35m'  # Purple
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'


def show_preload_banner():
    random_words = random.SystemRandom().choice([BANNER1, BANNER2])
    print(random_words.format(GNSL, REDL, WHSL, ENDL))

def menu():
     return """ {2}
 {0}[{1} 1 {0}] {2}  Сканируем IP в {0}[Shodan and Сensys]       {0}[{1} 16 {0}] {1} Массовый dump данных с {0}Shodan.        {0}[{1} 31 {0}] {2} IP logger для профи, {0}Firefox.
 {0}[{1} 2 {0}] {2}  Работаем с {0}[domain]                      {0}[{1} 17 {0}] {1} Графический мониторинг{0} сети.          {0}[{1} 32 {0}] {2} Загрузить {0}OSINT Pack.
 {0}[{1} 3 {0}] {2}  Собрать информацию о мобильном номере.   {0}[{1} 18 {0}] {2} Обновления и новости. Поддержка.      {0}[{1} 33 {0}] {2} Whois{0} [domain]
 {0}[{1} 4 {0}] {0}  Map DNS png.{2} В высоком разрешении.       {0}[{1} 19 {0}] {1} Фишинг mod {0}[Big Bro 8.0]              {0}[{1} 34 {0}] {2} База данных утечек.
 {0}[{1} 5 {0}] {2}  Извлечь геолокацию из фото.              {0}[{1} 20 {0}] {2} Поиск по ебальнику.                   {0}[{1} 35 {0}] {2} Mission: Impossible Mod.
 {0}[{1} 6 {0}] {2}  Поиск по фотографии.                     {0}[{1} 21 {0}] {2} OSINT Википедия.                      {0}[{1} 36 {0}] {2} Доступно в{0} PRO{2} версии.
 {0}[{1} 7 {0}] {2}  Проверка сервера на {0}[HoneyPot]           {0}[{1} 22 {0}] {1} Брутфорс {0}instagram.                   {0}[{1} 37 {0}] {2} Доступно в{0} PRO{2} версии.
 {0}[{1} 8 {0}] {2}  Mac address info.                        {0}[{1} 23 {0}] {2} Быстрая, анонимная {0}почта.             {0}[{1} 38 {0}] {2} Доступно в{0} PRO{2} версии.
 {0}[{1} 9 {0}] {2}  IP геолокация.                           {0}[{1} 24 {0}] {2} База данных паролей Bafomet +         {0}[{1} 39 {0}] {2} Доступно в{0} PRO{2} версии.
 {0}[{1} 10 {0}] {2} Проверить историю загрузок{0} [Torrent]     {0}[{1} 25 {0}] {1} Поднимаем сайт{0} Beff-XSS{0} в сеть.       {0}[{1} 40 {0}] {2} Доступно в{0} PRO{2} версии.
 {0}[{1} 11 {0}] {2} OSINT{0} Instagram.                         {0}[{1} 26 {0}] {2} Наше большое сообщество OSINT СНГ.    {0}[{1} 41 {0}] {2} Доступно в{0} PRO{2} версии.
 {0}[{1} 12 {0}] {2} DNS info.                                {0}[{1} 27 {0}] {1} Работаем с {0}[domain 2]                 {0}[{1} 42 {0}] {2} Доступно в{0} PRO{2} версии.
 {0}[{1} 13 {0}] {2} Найти адреса mail с любого сайта.        {0}[{1} 28 {0}] {1} Open{2}{0} Maltego.{0}                         {0}[{1} 43 {0}] {2} Доступно в{0} PRO{2} версии.
 {0}[{1} 14 {0}] {1} Подключение через{0} Android Debug Bridge.  {0}[{1} 29 {0}] {1} Массовый dump данных с {0}[ZoomEye]{0}.     {0}[{1} 44 {0}] {2} Техническая поддержка 24/7
 {0}[{1} 15 {0}] {1} Геолокация mod {0}[Big Bro 8.0]             {0}[{1} 30 {0}] {1} Деанон хакера,{0} его же ссылкой ngrok.  {0}[{1} 45 {0}] {0} Лицензионное соглашение. 

 {1}└──> {0} {2}Покинуть... {0}[{1} 0 {0}]{0}       {1}└──> {0} {2}Очистить...  {0}[{1} 66 {0}]{0}       {1}└──> {0} {2} Второе меню... {0}[{1} 88 {0}]{0}       {1}└──> {0} {2} Перезапуск... {0}[{1} 99 {0}]{0}
       """.format(GNSL, REDL, WHSL)

def main():
    os.system("printf '\033]2; OSINT SAN 3.5 \a'")
    os.system('clear')
    show_preload_banner()

    hardcoded_username = "osint"
    hardcoded_password = "san"

    while True:
        username = input(f"{R}\n └──> {G} Введите ваш ник{R}: ")
        print()

        if not username == hardcoded_username:
            print("  Username не найден в базе !!! Тааак ты что приложение спиздил ?")
            print("  Слышь кибер уебок, ")

            for i in range(6, -1, -1):
                print(f'\r  До отправки логов в  Отдел К   {i}', end='...')
                time.sleep(1)
        else:
            break

    for i in range(1, 6):
        password = getpass.getpass(f"{R} └──> {B} Введите ваш ключ доступа{R}: ")
        if password == hardcoded_password:
            print(f"{R} Вы успешно вошли в аккаунт")
            print(f"{R}  подождите 3 секунды до запуска .....")
            print(f"{G}  Ты красавчик")
            show_banner(clear=True)
            break
        else:
            print("На 5 попытку я отправлю твои логи в общий доступ на github,"
                  " и отформатирую системный диск")
            print(f"{i} Попытка...")
    else:
        print("Ну все, твои логи отправлены в github, отформатирование системного "
              "диска начнется через 5 минут...")

    repl_prompt.repl()

    os.system('clear')
    return


if __name__ == '__main__':
    main()
