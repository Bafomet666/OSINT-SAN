# -*- coding: utf-8 -*-
#Developer by Bafomet

from settings import phone_apis

import requests

# color
R = "\033[31m"    # Red
G = "\033[1;34m"  # Blue
C = "\033[1;32m"  # Green
W = "\033[0m"     # white
O = "\033[45m"    # Purple


def check_phone_api_token():
	if not phone_apis:
		return False

	return True


def phone_number(ph):
		print(f"{R} [ + ]{C} Получение сведений о телефонном номере...{C}\n")

		api_keys = phone_apis()

		clear_phone_number = "".join([i for i in ph if i.isdigit()])

		url = "http://apilayer.net/api/validate"
		for api_key in api_keys.split(","):
			try:
				response = requests.get(
					url,
					params={"access_key": api_key, "number": clear_phone_number}
				)

				result = response.json()

				if "error" in result.keys():
					continue

				elif not result["valid"]:
					print(f"{C} Ошибка: неверный номер мобильного телефона")
					return

				else:
					print(f"{R} [ + ]{C} Сам номер: {result['number']}")
					print(f"{R} [ + ]{C} Тип: {result['line_type']}")
					print(f"{R} [ + ]{C} Код страны: {result['country_code']}")
					print(f"{R} [ + ]{C} Страна: {result['country_name']}")
					print(f"{R} [ + ]{C} Геолокация: {result['location']}")
					print(f"{R} [ + ]{C} Оператор: {result['carrier']}")

					print()
					return 
			except:
				continue

		print(str(response.json()["error"]["info"]).split(".")[0])
