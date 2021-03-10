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
    22: information_services_data.page_restokz,
    23: information_services_data.page_aresti,
    24: information_services_data.page_uzbusa,
    25: information_services_data.page_scam_and_spam_nomber,
    26: information_services_data.page_reddit,
    27: information_services_data.page_facebook,
    28: information_services_data.page_suite_searche,
    29: information_services_data.page_system_claster,
    30: information_services_data.page_searche_system,
    31: information_services_data.page_msearche_system,
    32: information_services_data.page_twitter,
    33: information_services_data.page_doc_searche,
    34: information_services_data.page_flight_tracking,
    35: information_services_data.page_cryptocurrency_investigations,
    36: information_services_data.page_auto_searche,
    37: information_services_data.page_marine_cargo_tracking,
    38: information_services_data.page_forum,
    39: information_services_data.page_classifieds,
    40: information_services_data.page_events,
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
  {2}OSINT-SAN 3.5.2
  {0}Второй сезон.

  {0}[{1} 1 {0}] {2}  Nickname                   {0}[{1} 31 {0}] {2} Международные{0} поисковые системы   {0}[{1} 61 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 2 {0}] {2}  Mail и почта               {0}[{1} 32 {0}] {2} Twitter OSINT                     {0}[{1} 62 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 3 {0}] {2}  Мобильные номера           {0}[{1} 33 {0}] {2} Поиск документов                  {0}[{1} 63 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 4 {0}] {2}  Карты                      {0}[{1} 34 {0}] {2} Отслеживание полетов              {0}[{1} 64 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 5 {0}] {2}  Пользователь {0}Telegram      {0}[{1} 35 {0}] {2} Криптовалютные {0}расследования      {0}[{1} 65 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 6 {0}] {2}  Граждане {0}Белaруси          {0}[{1} 36 {0}] {2} Информация о автомобиле           {0}[{1} 66 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 7 {0}] {2}  Военнослужащие             {0}[{1} 37 {0}] {2} Морской и грузовой транспорт      {0}[{1} 67 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 8 {0}] {2}  Граждане {0}России            {0}[{1} 38 {0}] {2} Поиск {0}форумов                     {0}[{1} 68 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 9 {0}] {0}  Мониториг техники          {0}[{1} 39 {0}] {2} Объявления Европа                 {0}[{1} 69 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 10 {0}] {2} Социальные сети            {0}[{1} 40 {0}] {2} События Европа                    {0}[{1} 70 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 11 {0}] {2} Геолокация                 {0}[{1} 41 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 71 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 12 {0}] {2} Деанонимизация по лицу     {0}[{1} 42 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 72 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 13 {0}] {2} Instagram OSINT            {0}[{1} 43 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 73 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 14 {0}] {2} Offenosint OS              {0}[{1} 44 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 74 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 15 {0}] {2} VK OSINT                   {0}[{1} 45 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 75 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 16 {0}] {2} Nickname                   {0}[{1} 46 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 76 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 17 {0}] {2} Mail и почта               {0}[{1} 47 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 77 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 18 {0}] {2} Мобильные номера           {0}[{1} 48 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 78 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 19 {0}] {2} Карты                      {0}[{1} 49 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 79 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 20 {0}] {2} Ресурсы                       {0}[{1} 50 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 80 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 21 {0}] {2} Shodan запросы             {0}[{1} 51 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 81 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 22 {0}] {2} Граждане Казахстана        {0}[{1} 52 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 82 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 23 {0}] {2} Аресты, заключенные {0}USA    {0}[{1} 53 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 83 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 24 {0}] {2} Данные избирателя{0} USA      {0}[{1} 54 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 84 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 25 {0}] {2} Пров номера на {0}скам        {0}[{1} 55 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 85 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 26 {0}] {2} Reddit info                {0}[{1} 56 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 86 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 27 {0}] {2} Facebook OSINT             {0}[{1} 57 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 87 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 28 {0}] {2} Поиск похожих сайтов       {0}[{1} 58 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 88 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 29 {0}] {2} Cистемы кластеризации      {0}[{1} 59 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 89 {0}] {2} Доступно в{0} PRO{2} версии
  {0}[{1} 30 {0}] {2} Спец поисковые системы     {0}[{1} 60 {0}] {2} Доступно в{0} PRO{2} версии             {0}[{1} 90 {0}] {2} Доступно в{0} PRO{2} версии

  {1}└──> {0}{2}В главное меню. {0}[{1} 99 {0}]{0}
""".format(GNSL, REDL, WHSL, ENDL)


def show_page(page):
    while True:
        os.system("clear")
        print(information_services_data.banner)
        print(page)
        print(information_services_data.banner_end)

        try:
            option = input(f"{REDL}  └──>{ENDL} Введите 99 для выхода: {ENDL}")
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
