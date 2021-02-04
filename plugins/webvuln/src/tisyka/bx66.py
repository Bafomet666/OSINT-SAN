#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
import sys
import readline
# set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

page = '''{1} 
 _____ ___  _____  ______   ______  _____  ______   ______    322
| | | | | \  | |  / |      / |       | |  / |  | \ | |  \ \      
| | | | | |  | |  '------. '------.  | |  | |  | | | |  | |      
|_| |_| |_| _|_|_  ____|_/  ____|_/ _|_|_ \_|__|_/ |_|  |_|      
                                                                 
 
  {2} Ваша новая личность. Если вы возьметесь, за её выполнение.

  {0} Сафронов Эдуард Альбертович. Звание: Генирал Армии России.               Ваш кейс с новыми документами находится в точке сбора:
  
  {0} Дата рождения 15 апреля 1973 года                                        Г. Уйское, ул. Марксистский пер, дом 70, квартира 855

  {0} Телефон +7 (932) 415-35-51.                                              Секретная почта для обмена разведанными:

  {0} Цвет глаз " Ализариновый красный " Цвет волос черный.                    mddkreml@missincia.gov

  {2} Данные для входа в социальные сети.

  {0} Логин  Safronov449
  {0} Пароль EduardoSafronov449
  
 
  {0}[ {1}1{0} ] {2} Прослушать задание.     {0}[ {1}0{0} ] {2} Открыть геолокацию обьекта. 
'''.format(GNSL, REDL, WHSL)

def main():
    option = input(GNSL+"("+REDL + " menu " + GNSL + ")"+ENDL + " : ")
        
    while(1):
        if option == '1':
            os.system("mpg123 01.mp3")
            os.system("firefox https://www.google.com/maps/place/55%C2%B045'13.5%22N+37%C2%B037'12.1%22E/@55.7537328,37.6187555,18z/data=!4m13!1m7!3m6!1s0x0:0x0!2zNTXCsDQ4MTkuMCJOIDM3wrAzMjE0LjQiRQ!7e2!8m2!3d55.8052886!4d37.5373455!3m4!1s0x0:0x0!8m2!3d55.7536989!4d37.6199258?hl=ru")
            os.system("exit")
            exit()

        elif option == '0':
            os.system("firefox https://www.google.com/maps/place/%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9+%D0%9A%D1%80%D0%B5%D0%BC%D0%BB%D1%8C/@55.7526605,37.6170294,16.25z/data=!4m5!3m4!1s0x46b54a50b315e573:0xa886bf5a3d9b2e68!8m2!3d55.7520233!4d37.6174994?hl=ru")
            exit()
            break
        else:
            print("Спасибо за использование...")
            option = input(ENDL + ""+GNSL+"("+REDL + " menu " + GNSL + ")"+ENDL + "> ")

os.system("printf '\033]2;Ваша миссия, если вы возьметесь за её выполнение.\a'")
os.system('clear')
print(page)
main()
