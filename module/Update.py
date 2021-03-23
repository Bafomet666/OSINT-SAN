##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
from module.utils.banner import show_banner
#set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'
page_1 = '''{2}                                                                           
  Для установки обновления вам нужно, зайти в папку OSINT-SAN в которой будет находится новый клиент (OSINT-SAN)
  И скопировать оттуда содержимое, далее вставить с заменой файлов в основную папку OSINT-SAN,
  либо в другую любую папку, где вы будите использовать framework
             
  {1} [ {0}99{1} ] {2} В главное меню.    {1} [ {0}66{1} ] {2} Загрузить новый клиент.
'''.format(GNSL, REDL, WHSL)

def update():
    os.system("printf '\033]2;OSINT 3.5.5\a'")
    show_banner(clear=True)

    print(page_1)

    while True:
        option = input(f"{REDL}  └──>{ENDL} Введите опцию: {ENDL}")
        if option == '99':
            show_banner(clear=True)
            return
            
        if option == '66':
            print(f'\n Загрузка обновления OSINT-SAN. \n Скорость загрузки зависит от скорости интернета')
            os.system('git clone https://github.com/Bafomet666/OSINT-SAN')
            print(f'\n Обновленный клиент успешно загружен!')
            return
