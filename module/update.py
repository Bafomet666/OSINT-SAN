#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
from osintsan import menu
from module.utils.banner import show_banner

#set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

os.system("printf '\033]2;OSINT SAN 3.5\a'")
page_1 = '''{1}
 {2}Список изменений обновлений и инструкция по установке...   

 {0}Обновление загружается ввиде папки, После вам нужно скопировать все из папки update-osint
 в папку с самим framework заменой файлов.

 Но возможно могут слететь ваши API, заранее прошу извинения.
 Обновления выходят раз в месяц. Патчи могут выходить раз в две недели.

 {2}Дата последнего обновления 25 февраля.           

 {0}[ {1}99{0} ] {2}Выйти...       {0}[ {1}0{0} ] {2} Загрузить обновление...                  
  
'''.format(GNSL, REDL, WHSL)

def update():
    show_banner(clear=True)
    print(page_1)
    option = input(REDL + " └──>" + ENDL +" Введите 99 для возврата в меню :  ")
    
    while(1):
        if option == '99':
            return
            return

        elif option == '0':
            print(("{1}[ {0}+{1} ]{2} Загрузка с github...{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("git clone https://github.com/Bafomet666/OSINT-SAN")
            menu()
            break
            
        else:
            show_banner(clear=True)
            break
try:
    update()

except KeyboardInterrupt:
    sys.exit(1)
except KeyboardInterrupt:
        print ("Ctrl+C pressed...")
