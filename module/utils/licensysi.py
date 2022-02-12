import json
import os
import sys
from module.utils import COLORS
from module.utils.ban import page_licence
from core.core import clear_screen


def show_licence():
    clear_screen()
    print(page_licence)


def check_licence(path_to_licence):
    if not os.path.exists(path_to_licence):
        return False
    with open(path_to_licence, 'r') as f:
        data = json.load(f)

    if 'licence' in data and data['licence']:
        return True
    else:
        return False


def agree_licence(path_to_licence):
    with open(path_to_licence, 'w') as f:
        json.dump({'licence': True}, f)


def licence(path_to_licence):
    show_licence()
    inputted = input(f"{COLORS.REDL}  Для подтверждения лицензии нажмите enter: ")
    if inputted == '99':
        sys.exit()
    agree_licence(path_to_licence)
