#Developer by Bafomet
# -*- coding: utf-8 -*-
'''
Редактировал код l3e86
'''
import os
import requests
import json
import time
import getpass
import subprocess
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

class ZoomEye(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

        self.access_token = ''
        # self.zoomeye_login_api = "https://api.zoomeye.org/user/login"
        # self.zoomeye_dork_api = "https://api.zoomeye.org/{}/search"

        self.ip_port_list = []

        self.load_access_token()

    def load_access_token(self):
        if not os.path.isfile('access_token.txt'):
            print("")
            print(WHSL +" Давай щас войдем в твой аккаунт, для осуществления поиска, здесь аккаунт и есть API.")
            print("")
            print(WHSL +" Все данные сохраняться по пути OSINT-SAN/module Название файла")
            self.login()
        else:
            with open('access_token.txt', 'r') as fr:
                self.access_token = fr.read()

    def save_access_token(self):
        with open('access_token.txt', 'w') as fw:
            fw.write(self.access_token)

    def login(self):
        """
        Предлагаю ввести имя учетной записи и пароль
        :return: None
        """
        try:
            print("")
            self.username = input(REDL+ " [ + ] " + WHSL + " username: ").strip()
            print("")
            #l3e86: добавил фичу скрытого ввода пароля           
            self.password = getpass.getpass(REDL+ " [ + ] " + WHSL + " password: ").strip()
            
        #l3e86: классика, если нажимаем 0 то идем в ядро, ентр 
        except KeyboardInterrupt:
            print("")
            choise_exit = input('\n [ + ] Eсли нужно выйти в главное меню, введите, Enter, чтобы продолжить работать с модулем:')
            if choise_exit == '0':
                #l3e86: переход к ядру во всех других случаях возврат к идентификации
                os.system("cd ..;python3 osintsan.py")
            else:
                self.login()
                    
        data = {
            'username': self.username,
            'password': self.password
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }

        # выгружает объекты Python в строки JSON
        data_encoded = json.dumps(data)
        try:
            resp = requests.post(url='https://api.zoomeye.org/user/login', data=data_encoded, headers=headers)
            # Преобразование строки json в объект python
            r_decoded = json.loads(resp.text)

            # Получите access_token аккаунта
            access_token = r_decoded['access_token']
            self.access_token = access_token
            self.save_access_token()
            print("")
            print(REDL+' Авторизация успешно пройдена ...')
            print("")
        except:
            print(' [ + ] Неверное имя пользователя или пароль, попробуйте еще раз ')
            #l3e86: если логин и пароль введены не правильно 
            #запрашиваем еще раз, до тех пор пока не будет введен правильный лог\пасс
            self.login()
            #exit()

    def search(self):

        if not self.access_token:
            self.login()

        # Отформатируйте токен и добавьте его в заголовок HTTP.
        headers = {
            'Authorization': 'JWT ' + self.access_token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }

        #l3e86: добавил бесконечный цикл на ввод запросов
        #обработка исключения, при котором пользователь выйдет из модуля
        #для дольнейшей работы с osintSan
        while True:
            try:
                # Строка для поиска  query = 'port:80 weblogic country:China'
                print("")
                query = input(REDL + " └──> "+ WHSL +" Вводи поисковой запрос "+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + ": ")

                # Установите начальную страницу для получения результатов, что более полезно, когда сумма относительно велика
                print("")
                page = int(input(REDL + " └──>"+ WHSL +"  С какой страницы начать ? введи номер "+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + ": "))

                # Установите количество страниц результатов
                print("")
                num = int(input(REDL + " └──> "+ WHSL +" Введите количество страниц, которые вы хотите получить "+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + ": "))

                index = 0
                while True:
                    try:
                        # Объедините строку запроса и номер страницы для создания URL
                        if index == num:
                            break
                        print("")
                        msg = GNSL +' [{}/{}] Получаю страницу: {}'.format(index+1, num, page)
                        print(msg)

                        api = 'https://api.zoomeye.org/host/search'
                        # searchurl = '{}{}&page={}'.format(api, query, page)
                        print("")
                        print(WHSL +' Вывожу запрос :', query)
                        print("")

                        # Используется для получения результатов на следующей странице
                        page += 1
                        index += 1

                        resp = requests.get(api, headers=headers, params={"query": query, "page": page})
                        r_decoded = json.loads(resp.text)
                        for x in r_decoded['matches']:
                            print(x['ip'], ':', x['portinfo']['port'])
                            self.ip_port_list.append(x['ip'] + ':' + str(x['portinfo']['port']))
                    except Exception as e:
                        # Если поисковый запрос превышает максимальный предел входа, разрешенный API, или поиск завершается, запрос будет прекращен.
                        if str(e) == 'matches':
                            print(' [ + ] info : Аккаунт был остановлен, превыны максимальные ограничения')
                            break
                        else:
                            print(' [ + ] info : ', str(e))
                self.save_result()
                pass
                
            #l3e86: собственно сама кнопка
            except KeyboardInterrupt:
                print("")
                choise_exit = input('\n [ + ] Eсли нужно выйти в главное меню нажмите 99 или Enter, чтобы продолжить работать с модулем:')
                if choise_exit == '0':
                    #l3e86: возврат к ядру
                    os.system("cd ..;python3 osintsan.py")
                else:
                    pass

    def save_result(self):
        # Создайте файл во время выполнения сценария в данный момент, чтобы вы могли убедиться, что файл, созданный при запуске сценария, не будет иметь того же имени.
        xtime = time.strftime("[%Y-%m-%d][%H.%M.%S]")
        ip_port_list_file = '{}.txt'.format(xtime)

        #  Записать ip: порт в файл
        with open(ip_port_list_file, 'w') as fw:
            for line in self.ip_port_list:
                fw.write(line + '\n')
        pass


if __name__ == '__main__':
    zoomeye = ZoomEye()
    zoomeye.search()
    pass

