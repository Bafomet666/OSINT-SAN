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
WHSL = C = "\033[32;1m"
ENDL = W = "\033[0m"
REDL = R = "\033[0;31m"
GNSL = G = "\033[1;34m"
WHITEL = B = "\033[39m"
O = "\033[45m"

def show_preload_banner():
    random_words = random.SystemRandom().choice([BANNER1, BANNER2])
    print(random_words.format(GNSL, REDL, WHSL, ENDL))

def menu():
     return """ {2}
 {0}[{1} 1 {0}] {2}  Сканировать IP в {0}[Shodan and Сensys]      {0}[{1} 16 {0}] {2} Сбор данных с помощью {0}[Shodan]     {1}| {2} Обновить клиент  {0}[{1} 55 {0}]
 {0}[{1} 2 {0}] {2}  Получить информацию о {0}[domain]            {0}[{1} 17 {0}] {1} Мониторинг локальной сети          {1}| {2} Поддержка 24/7   {0}[{1} 65 {0}]
 {0}[{1} 3 {0}] {2}  Собрать информацию о мобильном номере     {0}[{1} 18 {0}] {2} Проверить все плагины              {1}| {2} Второе меню      {0}[{1} 88 {0}]
 {0}[{1} 4 {0}] {2}  Карта{0} DNS{2} в высоком разрешении            {0}[{1} 19 {0}] {1} Mod фишинг {0}[Big Bro 8.0]           {1}| {2} Перезапуск       {0}[{1} 99 {0}]
 {0}[{1} 5 {0}] {2}  Вычисление места съёмки фотографии        {0}[{1} 20 {0}] {2} Идентифика́ция по лицу              {1}| {2} Очистить         {0}[{1} 75 {0}]
 {0}[{1} 6 {0}] {2}  Поиск по фотографии                       {0}[{1} 21 {0}] {2} OSINT {0}Википедия                    {1}| {2} Покинуть         {0}[{1} 00 {0}]
 {0}[{1} 7 {0}] {2}  Проверка IP address на {0}[HoneyPot]         {0}[{1} 22 {0}] {2} IP logger                          {1}|                              
 {0}[{1} 8 {0}] {2}  Mac address info                          {0}[{1} 23 {0}] {2} Анонимная почта                    {1}| 
 {0}[{1} 9 {0}] {0}  IP and domian {2}геолокация                  {0}[{1} 24 {0}] {2} База данных паролей Bafomet +         
 {0}[{1} 10 {0}] {2} Проверить историю загрузок{0} [Torrent]      {0}[{1} 25 {0}] {0} Beff-XSS{2} + ngrok 
 {0}[{1} 11 {0}] {2} OSINT{0} Instagram                           {0}[{1} 26 {0}] {2} Сообщество OSINT 
 {0}[{1} 12 {0}] {2} Подробная информация о {0}DNS                {0}[{1} 27 {0}] {2} Загрузить {0}OSINT Pack {0}1.0
 {0}[{1} 13 {0}] {2} Поиск {0}@mail{2} адресов на сайтах             {0}[{1} 28 {0}] {1} Открыть{2}{0} Maltego {0}                   
 {0}[{1} 14 {0}] {1} Подключение через{0} [Android Debug Bridge]  {0}[{1} 29 {0}] {2} Сбор данных с помощью {0}[ZoomEye]{0}
 {0}[{1} 15 {0}] {1} Определение геолокации {0}[Big Bro 8.0]      {0}[{1} 30 {0}] {1} Деанонимизация хакера через{0} ngrok 
""".format(GNSL, REDL, WHSL) 

def main():
    os.system("printf '\033]2; OSINT SAN 3.5 \a'")
    os.system('clear')
    show_preload_banner()

    hardcoded_username = "osint"
    hardcoded_password = "san"

    while True:
        username = input(f"{R}\n └──> {G} Введите ваш ник{R}:{B} ")
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
        password = getpass.getpass(f"{R} └──> {B} Введите ваш ключ доступа{R}:{B} ")
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
