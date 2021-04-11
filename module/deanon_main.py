##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet and l3e86
from module import deanon_mod
from module.utils import COLORS
from osintsan import menu

def deanon_menu():
    while True:
        print()
        print(f"{COLORS.REDL} [ + ] {COLORS.WHSL}  Выберите опцию")
        print()

        # эквевалент -p
        print(f"{COLORS.REDL} [ 1 ] {COLORS.WHSL}  Парсинг железа")

        # эквевалент -с
        print(f"{COLORS.REDL} [ 2 ] {COLORS.WHSL}  Крашнуть ngrok противника")

        # эквевалент -l
        print(f"{COLORS.REDL} [ 3 ] {COLORS.WHSL}  Отследить геолокацию")

        print(f"{COLORS.REDL} [ 4 ] {COLORS.WHSL}  Выйти с перезапуском")

        # запрос у пользователя на ввод операции
        print()
        try:
            user_input = input(f"{COLORS.REDL} └──>{COLORS.GNSL}   [{COLORS.WHSL} main_menu {COLORS.GNSL}]{COLORS.ENDL}: ")

            # запрос урла, проверка на пустую строку
            # и если она пустая то возвращаемся в главное меню
            # можно попробовать к вводу урла, но я и так проебал пол дня,
            # весь мозг выстраивая эту ахуенную конструкцию, но если попросишь перепишу
            print()
            url = input(f"{COLORS.REDL} [ + ] {COLORS.WHSL}  Укажите url :").strip()
            # обработчик ошибок тут все ясно
        except KeyboardInterrupt:
            print()
            try:
                choice_exit = input(
                    f"{COLORS.REDL} [ + ] {COLORS.WHSL} Что-бы вернутся в меню нажмите 0, либо ctrl + c"
                )
                menu()
            except KeyboardInterrupt:
                break

            if choice_exit == '0':
                continue

            else:
                print('\n[!] пока\n')
                return

        print()
        if url == '':
            print('\n[-] Неверное значение')
        if not url.startswith("http"):
            print("\n[-] Ты забыл указать схему (`http` или `https`)")

        else:
            if user_input == '1':
                deanon_mod.parse_info(url)

            elif user_input == '2':
                deanon_mod.destroy_ngrok(url)

            elif user_input == '3':
                # условие где переменная time(тайминг)
                # инициализируется дефолтным значением
                # при условии пустой строки
                try:
                    time = input('Укажите задержку в минутах по умолчанию 180минут: ')
                except KeyboardInterrupt:
                    continue

                if not time:
                    time = 180 * 60
                else:
                    time = float(time) * 60

                deanon_mod.trace_geo(time, url)

            elif user_input == '4':
                menu()

    print('\n[!] пока\n')


if __name__ == '__main__':
    deanon_menu()
