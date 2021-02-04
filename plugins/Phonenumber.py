from plugins.api import phoneapis
import requests
#Developer by Bafomet
# -*- coding: utf-8 -*-
#color
R = "\033[31m"   # Red
G = "\033[1;34m" # Blue
C = "\033[1;32m" # Green
W = "\033[0m"    # white
O = "\033[45m"   # Purple

def Phonenumber(ph):
		print(R + " [ + ]" + C +" Получение сведений о телефонном номере..." + C +"\n")
		apikey=phoneapis()
		if apikey == "":
				print(C +" Добавьте ключ API phoneapis")
				exit()
		ph="".join([i for i in ph if i.isdigit()])
		for api_key in apikey.split(","):
			url = ("http://apilayer.net/api/validate?access_key="+api_key+"&number="+str(ph))
			try:
				response=requests.get(url)
				if "error" in response.json().keys():
					continue
				elif response.json()["valid"]==False:
					print(C +" Ошибка: неверный номер мобильного телефона")
					return
				else:
					get=response.json()
					print(R +" [ + ]" + C + " Сам номер: "+get["number"])
					print(R +" [ + ]" + C + " Тип: "+get["line_type"])
					print(R +" [ + ]" + C + " Код страны: "+get["country_code"])
					print(R +" [ + ]" + C + " Страна: "+get["country_name"])
					print(R +" [ + ]" + C + " Геолокация: "+get["location"])
					print(R +" [ + ]" + C + " Оператор: "+get["carrier"])
					print("")
					return 
			except:
				continue
		print(str(response.json()["error"]["info"]).split(".")[0])
				
