#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os

from module import information_services_data

#set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'


option_to_page = {
    1: information_services_data.page_nicknames_2,
    2: information_services_data.page_mail,
    3: information_services_data.page_numbers,
    4: information_services_data.page_maps,  
    5: information_services_data.page_telegram_osint,
    6: information_services_data.page_br_gov,   
    7: information_services_data.page_millitary,
    8: information_services_data.page_ru_gov,
    9: information_services_data.page_equipment,
    10: information_services_data.page_social_osint,
    11: information_services_data.page_sun_geolocation, 
    12: information_services_data.page_deanon_face,
    13: information_services_data.page_instagram_osint,
    14: information_services_data.page_offenosint,
    15: information_services_data.page_vk_osint,
    16: information_services_data.page_restore,
    17: information_services_data.page_ip,
    18: information_services_data.page_browsers,
    19: information_services_data.page_fio,
    20: information_services_data.page_resources,
    21: information_services_data.page_shodan,
}

# переместим в information_services_data, а вообще стоит его переименовать, да
TO_BANNER = """{1}

  $$\      $$\ $$\ $$\       $$\                           $$\ $$\                  $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ $$$$$$$$\ 
  $$ | $\  $$ |\__|$$ |      \__|                          $$ |\__|                $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |\__$$  __|
  $$ |$$$\ $$ |$$\ $$ |  $$\ $$\  $$$$$$\   $$$$$$\   $$$$$$$ |$$\  $$$$$$\        $$ /  $$ |$$ /  \__|  $$ |  $$$$\ $$ |   $$ |   
  $$ $$ $$\$$ |$$ |$$ | $$  |$$ |$$  __$$\ $$  __$$\ $$  __$$ |$$ | \____$$\       $$ |  $$ |\$$$$$$\    $$ |  $$ $$\$$ |   $$ |   
  $$$$  _$$$$ |$$ |$$$$$$  / $$ |$$ /  $$ |$$$$$$$$ |$$ /  $$ |$$ | $$$$$$$ |      $$ |  $$ | \____$$\   $$ |  $$ \$$$$ |   $$ |   
  $$$  / \$$$ |$$ |$$  _$$<  $$ |$$ |  $$ |$$   ____|$$ |  $$ |$$ |$$  __$$ |      $$ |  $$ |$$\   $$ |  $$ |  $$ |\$$$ |   $$ |   
  $$  /   \$$ |$$ |$$ | \$$\ $$ |$$$$$$$  |\$$$$$$$\ \$$$$$$$ |$$ |\$$$$$$$ |       $$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |   $$ |   
  \__/     \__|\__|\__|  \__|\__|$$  ____/  \_______| \_______|\__| \_______|       \______/  \______/ \______|\__|  \__|   \__|   
                                 $$ |                                                                                              
                                 $$ |                                                                                              
                                 \__|                                                                                                                                       
  {0}OST OSINT-SAN 3.5
  {0}Первый сезон.

  {0}[{1} 1 {0}] {2}  Nickname.                     {0}[{1} 16 {0}] {2} Восстановление доступа.  {0}[{1} 31 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 2 {0}] {2}  Mail и почта.                 {0}[{1} 17 {0}] {2} OSINT {0}IP Info.           {0}[{1} 32 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 3 {0}] {2}  Мобильные номера.             {0}[{1} 18 {0}] {2} Работа с Браузером.      {0}[{1} 33 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 4 {0}] {2}  Карты.                        {0}[{1} 19 {0}] {2} Поиск по {0}ФИО{2} гражд РФ.   {0}[{1} 34 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 5 {0}] {2}  Пользователь {0}Telegram.        {0}[{1} 20 {0}] {2} Ресурсы.                 {0}[{1} 35 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 6 {0}] {2}  Граждане {0}Белоруси.            {0}[{1} 21 {0}] {2} Shodan запросы.          {0}[{1} 36 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 7 {0}] {2}  Военнослужащие.               {0}[{1} 22 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 37 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 8 {0}] {2}  Граждане России.              {0}[{1} 23 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 38 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 9 {0}] {0}  Мониториг техники             {0}[{1} 24 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 39 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 10 {0}] {2} Социальные сети.              {0}[{1} 25 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 40 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 11 {0}] {2} Геолокация.                   {0}[{1} 26 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 41 {0}] {2} Доступно в{0} PRO{2} версии..
  {0}[{1} 12 {0}] {2} Деанонимизация по лицу.       {0}[{1} 27 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 42 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 13 {0}] {2} Instagram OSINT.              {0}[{1} 28 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 43 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 14 {0}] {2} Offenosint OS                 {0}[{1} 29 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 44 {0}] {2} Доступно в{0} PRO{2} версии.
  {0}[{1} 15 {0}] {2} VK OSINT                      {0}[{1} 30 {0}] {2} Доступно в{0} PRO{2} версии.   {0}[{1} 45 {0}] {2} Доступно в{0} PRO{2} версии.

  {1}└──> {0} {2} В главное меню. {0}[{1} 99 {0}]{0}
""".format(GNSL, REDL, WHSL, ENDL)


def show_page(page):
    while True:
        os.system("clear")
        print(information_services_data.banner)
        print(page)
        print(information_services_data.banner_end)

        try:
            option = input(f"{REDL}  └──>{ENDL} Введите 99 для выхода : {ENDL} ")
        except KeyboardInterrupt:
            break

        if option == "99":
            break


def information_menu():
    while True:
        os.system("clear")
        print(TO_BANNER)
        try:
            option = input(f"{REDL}  └──>{ENDL} Введите 99 для выхода : {ENDL} ")
        except KeyboardInterrupt:
            return

        try:
            page = int(option)
        except ValueError:
            continue

        if page == 99:
            return
        else:
            page = option_to_page.get(page)
            if page:
                show_page(page)


if __name__ == '__main__':
    information_menu()
