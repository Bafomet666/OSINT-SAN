from module.utils.banner import show_banner

try:
    from module import api
except ImportError:
    from . import api

#By bafomet
#By I3e86
# Set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'


def search_through_instagram():
    while True:
        try:
            print()
            show_banner(clear=True)
            user_name = input(f"{REDL} └──>{WHSL} Введите username instagram {GNSL}[{REDL}main_menu{GNSL}]{ENDL}:")
            print()
            print(f' Если вдруг выбьет ошибку: json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) Просто смени IP address')
            input(f"{GNSL} [ {REDL}Напоминание{GNSL} ]{WHSL} Если захочешь выйти, введи 99. Нажми enter что бы продолжить{ENDL}:")
            if user_name == '99':
                show_banner(clear=True)
                return
            elif user_name == '':
                print('  [ - ] Некоректный ввод username')
            else:
                api.user_info(user_name)

        except KeyboardInterrupt:
            print('\nпока!')
            break


if __name__ == '__main__':
    search_through_instagram()
