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
page_1 = '''{1}                                                                           
  {2}Список паролей разбит на файлы. Там много архивов. {2}

  {2}Сейчас общий вес 10 гб.{2}
  
  Часть вы можете загрузить:

  {1}[ {0}+{1} ]{2} 1.5 миллиардов паролей{2} {1} https://mega.nz/file/9GhkwBLK#nNj5L6qPMGT679lGRjpZFV-kG0kx2m8VXMrmoTUe7cQ {1}   
  
  {1}[ {0}+{1} ]{2} 14 млн паролей, 250 МБ, зеркало {2}
  
  {0}SHA1 hash of the 7-Zip file: 00fc585efad08a4b6323f8e4196aae9207f8b09f{0}
  {0}SHA1 hash of the text file: 3fe6457fa8be6da10191bffa0f4cec43603a9f56{0} 
  {1}https://downloads.pwnedpasswords.com/passwords/pwned-passwords-update-1.txt.7z{1}
  
  {1}[ {0}+{1} ]{2} 306 млн паролей, 5,3 ГБ, зеркало {2}
  
  {0}SHA1 hash of the 7-Zip file: 90d57d16a2dfe00de6cc58d0fa7882229ace4a53 {0}
  {0}SHA1 hash of the text file: d3f3ba6d05b9b451c2b59fd857d94ea421001b16 {0}
  {1}https://downloads.pwnedpasswords.com/passwords/pwned-passwords-1.0.txt.7z{1}

  {1}[ {0}+{1} ]{2} Словари для брута wifi сетей. Проверьте поледнее на virus total{2} 
  
  {1}https://yadi.sk/d/O5FQG3B4zNmS5Q {1}

  {2}10 млн паролей {2}

  {1}https://mega.nz/file/EOgwzShJ#lp7hZj9yJefSbUhooGjb_ohTPLAF_upt6Yd_BZ-qSf4 {1}
  
  {2}Внизу еще пароли.
  
  {1}https://github.com/Bafomet666/password_one
  
  {0}[ {1}99{0} ] {2}Выйти...                 
  
'''.format(GNSL, REDL, WHSL)


def password_menu():
    os.system("printf '\033]2;OSINT 3.5\a'")
    show_banner(clear=True)

    print(page_1)

    while True:
        option = input(f"{REDL}  └──>{ENDL} Введите 99 для выхода : {ENDL} ")
        if option == '99':
            print()
            print(" {1} [{0} + {1}]{2} Спасибо за использование нашего Exploit.".format(REDL, GNSL, WHSL))
            return
