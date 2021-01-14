from plugins.api import phoneapis
import requests
#Developer by Bafomet
#color
R = '\033[31m'   # Red
G = '\033[1;34m' # Blue
C = '\033[1;32m' # Green
W = '\033[0m'    # white
O = '\033[45m'   # Purple

def Phonenumber(ph):
		print (R + '[ + ]' + C +' Получение сведений о телефонном номере...' + C +'\n')
		apikey=phoneapis()
		if apikey == "":
				print("Add you phoneapis api key to src/api.py")
				exit()
		ph=''.join([i for i in ph if i.isdigit()])
		for api_key in apikey.split(","):
			url = ("http://apilayer.net/api/validate?access_key="+api_key+"&number="+str(ph))
			try:
				response=requests.get(url)
				if 'error' in response.json().keys():
					continue
				elif response.json()['valid']==False:
					print("Error: Invalid Mobile Number")
					return
				else:
					get=response.json()
					print(R +"[ + ] Сам номер: "+get['number'])
					print(R +"[ + ] Тип: "+get['line_type'])
					print(R +"[ + ] Код страны: "+get['country_code'])
					print(R +"[ + ] Страна: "+get['country_name'])
					print(R +"[ + ] Геолокация: "+get['location'])
					print(R +"[ + ] Оператор: "+get['carrier'])
					print("")
					return 
			except:
				continue
		print(str(response.json()['error']['info']).split(".")[0])
				
