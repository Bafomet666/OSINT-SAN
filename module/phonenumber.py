# -*- coding: utf-8 -*-
# Developer by Bafomet

from osintsan import phone_apis
from module.utils import COLORS
import requests


def check_phone_api_token():
    if not phone_apis:
        return False
    return True


def phone_number(ph):
    clear_phone_number = "".join([i for i in ph if i.isdigit()])

    url = "http://apilayer.net/api/validate"
    for api_key in phone_apis.split(","):
        try:
            response = requests.get(
                url,
                params={"access_key": api_key, "number": clear_phone_number}
            )

            result = response.json()

            if "error" in result.keys():
                continue

            elif not result["valid"]:
                print(f"{COLORS.GNSL} Ошибка: неверный номер мобильного телефона")
                return

            else:
                print(f"{COLORS.GNSL} [{COLORS.REDL} +{COLORS.GNSL} ]{COLORS.WHSL} Сам номер: {result['number']}")
                print(f"{COLORS.GNSL} [{COLORS.REDL} +{COLORS.GNSL} ]{COLORS.WHSL} Тип: {result['line_type']}")
                print(
                    f"{COLORS.GNSL} [{COLORS.REDL} +{COLORS.GNSL} ]{COLORS.WHSL} Код страны: {result['country_code']}")
                print(f"{COLORS.GNSL} [{COLORS.REDL} +{COLORS.GNSL} ]{COLORS.WHSL} Страна: {result['country_name']}")
                print(f"{COLORS.GNSL} [{COLORS.REDL} +{COLORS.GNSL} ]{COLORS.WHSL} Геолокация: {result['location']}")
                print(f"{COLORS.GNSL} [{COLORS.REDL} +{COLORS.GNSL} ]{COLORS.WHSL} Оператор: {result['carrier']}")
                print(f'\n{COLORS.REDL}---------------------------------------------------------------------------------------')
                return
        except:
            continue
