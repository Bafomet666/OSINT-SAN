from module.utils import COLORS
from pyngrok.conf import PyngrokConfig
from module.utils.ban import page_45
import time
import os 
from pyngrok import ngrok


def driver():
    print(page_45)
    install = input(f"{COLORS.REDL}  └──>{COLORS.WHSL} Нужна установка Google Chrome браузераа для модуля Big Borther y/n? :{COLORS.WHSL} ")
    if install == 'y':
         print(f'\n Загрузка chromium браузера\n')
         os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
         print(f'\n Установка\n')
         os.system('sudo apt install ./google-chrome-stable_current_amd64.deb')
               
    else:
         pass
             
    print(f'\n {COLORS.REDL} -------------------------------------------------------------------------')
    print(f'\n {COLORS.WHSL} Нам нужно выбрать приоритетный браузер ?\n  Для модуля Big Brother нужен браузер Google Chrome')
    browser = input(f"\n{COLORS.REDL}  └──>{COLORS.WHSL} Запускаем выбор y/n? : ")
    if browser == 'y':
         print(f'\n Выберите приоритетный браузер{COLORS.WHSL} \n')
         os.system('sudo update-alternatives --config x-www-browser')
               
    else:
         pass

    print(f' {COLORS.REDL} -------------------------------------------------------------------------')
    print(f'\n {COLORS.WHSL} Обновление и установка pycurl, tools, grub, requerements.txt')
    requer = input(f"\n{COLORS.REDL}  └──>{COLORS.WHSL} Обновим все зависимости python3 y/n? : ")
    if requer == 'y':
         os.system('pip3 install setuptools')
         os.system('pip3 install pycurl')
         os.system('pip3 install grab')
         os.system('sudo pip3 install -r requerements.txt')
               
    else:
         pass
                
                
    skikerpack = input(f"\n{COLORS.REDL}  └──>{COLORS.WHSL} Давай установим стикеры в terminal ? y/n? :{COLORS.WHSL} ")
    if skikerpack == 'y':
         os.system('sudo apt-get install -y fonts-noto-color-emoji')
         os.system('sudo apt-get update -y')
         print(f'\n Установка успешна')         
         print(f' {COLORS.REDL} -------------------------------------------------------------------------') 
    else:
         pass
         print(f' {COLORS.REDL} -------------------------------------------------------------------------')

    adb_server = input(f"\n{COLORS.REDL}  └──>{COLORS.WHSL} Install Android Debug Bridge protocol 📲 ? y/n? : ")
    if adb_server == 'y':
        os.system('sudo apt-get install android-tools-adb android-tools-fastboot')
    else:
         pass

    dop_tools = input(f"\n{COLORS.REDL}  └──>{COLORS.WHSL} Установка доп инструментов ? y/n? :{COLORS.WHSL} ")
    if dop_tools == 'y':
         os.system('sudo apt install metagoofil')
         os.system('sudo apt-get install install deepin-terminal') 

    else:
         pass
            
    ngrok = input(f"\n{COLORS.REDL}  └──>{COLORS.WHSL} Проводим установку Ngrok и всех его зависимостей ? y/n? :{COLORS.WHSL} ")
    if ngrok == 'y':
         os.system('pip3 install pyngrok')
         os.system('ngrok')
         print(f'\n{COLORS.WHSL} Токен вы можете взять в личном кабинете на сайте:{COLORS.FIOL} https://dashboard.ngrok.com/\n')
         token = input(f' Введите пользовательский token: ')
         os.system(f'ngrok authtoken {token} ')
         print(f'\n {COLORS.REDL}Токен успешно установлен, можете приступать к работе')

    else:
         pass
