# Developer by Bafomet
# -*- coding: utf-8 -*-

import shodan
import time
import json
import requests
import random
from osintsan import shodan_api_key, torrent_api
from module.utils import COLORS
from selenium import webdriver

shodan_api = shodan_api_key
torrent_api = torrent_api


def ip_info(ip):
    UA_list = [x.strip() for x in open('module/utils/user_agent.txt').readlines()]
    user_agent = random.choice(UA_list)

    # user_agent for Selenium
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent)
    opts = Options()
    opts.headless = True
    br = webdriver.Firefox(profile, options=opts)

    # user_agent for REQUESTS
    session = requests.Session()
    session.headers.update({'User-Agent': user_agent})

    api = shodan.Shodan(shodan_api)
    # ip = input(f"{COLORS.REDL} └──>{COLORS.GNSL} Введите IP адрес:{COLORS.WHSL} ")

    if not shodan_api:
        print(f"{COLORS.REDL}API ключ Shodan'а невалиден! (settings.py){COLORS.REDL}")
    try:
        api.info()
    except shodan.APIError:
        print(f"{COLORS.REDL}API ключ Shodan'а невалиден! (settings.py){COLORS.REDL}")

    try:
        host = api.host(ip)
        print(f' \n{COLORS.REDL} Глобальный поиск информации по IP \n')
        print(f"{COLORS.GNSL} [ + ] {COLORS.REDL} Получена информация с Shodan. \n")
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} IP Address ----: " + str(host["ip_str"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Страна  -------: " + str(host["country_name"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Город----------: " + str(host["city"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Организация  --: " + str(host["org"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} ISP -----------: " + str(host["isp"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Открытые порты : " + str(host["ports"]))
    except:
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} На сервисах Shodan нечего не найдено. ")
        print("")

    try:
        dirty_response = session.get(f'https://censys.io/ipv4/{ip}/raw').text
        clean_response = dirty_response.replace('&#34;', '"')
        x = clean_response.split('<code class="json">')[1].split('</code>')[0]
        censys = json.loads(x)
        print("")
        print(f"{COLORS.GNSL} [ + ] {COLORS.REDL} Получена информация с Censys. \n")
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Страна -------> " + str(censys["location"]["country"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Континент-----> " + str(censys["location"]["continent"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Код страны -- > " + str(censys["location"]["country_code"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Широта  ------> " + str(censys["location"]["latitude"]))
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} Долгота  -----> " + str(censys["location"]["longitude"]))
    except:
        print(f"{COLORS.GNSL} [ + ] {COLORS.WHSL} На сервисах Censys нечего не найдено. ")
        print("")

    # url = f"https://api.shodan.io/labs/honeyscore/{ip}"
    try:
        result: str = session.get(f"https://api.shodan.io/labs/honeyscore/{ip}", params={"key": shodan_api}).text
    except:
        print(f"\n {COLORS.GNSL}Нет доступной информации")
    if "error" in result or "404" in result:
        print(f"{COLORS.GNSL} IP address не найден")
    elif result:
        robability = str(float(result) * 10)
        print(f' \n{COLORS.REDL} ==================================================================================')
        print(f" \n{COLORS.GNSL} IP address просканирован лабораторией Shodan")
        print(
            f" \n{COLORS.GNSL} Вероятность что по данному IP address установлена ловушка:{COLORS.REDL} {robability}% ")
        print(f' \n{COLORS.REDL} ==================================================================================')

    r = session.get("https://api.antitor.com/history/peer/", params={"ip": ip, "key": torrent_api})
    res = r.json()
    print(f"\n{COLORS.REDL} Информация по загрузкам Torrent \n")
    if len(res) > 4:
        print(f" {COLORS.WHSL}IP address:{COLORS.GNSL}  {res['ip']}")
        print(f" {COLORS.WHSL}Провайдер :{COLORS.GNSL}  {res['isp']}")
        geo_data = res['geoData']
        print(f" {COLORS.WHSL}Страна    :{COLORS.GNSL}  {geo_data['country']}")
        print(f' {COLORS.REDL}\n Примерные координаты жертвы по мнению shodan\n')
        print(f" {COLORS.WHSL}Широта    :{COLORS.GNSL}  {geo_data['latitude']}")
        print(f" {COLORS.WHSL}Долгота   :{COLORS.GNSL}  {geo_data['longitude']}\n")
        print(f' {COLORS.REDL}\n Загружает в данный момент:\n')
        for i in res["contents"]:
            print('')
            print(f" {COLORS.WHSL}Каталог   :  {COLORS.GNSL}{i['category']}")
            print(f" {COLORS.WHSL}Имя       :  {COLORS.GNSL}{i['name']}")
            print(f" {COLORS.WHSL}Начало    :  {COLORS.GNSL}{i['startDate']}")
            print(f" {COLORS.WHSL}Конец     :  {COLORS.GNSL}{i['endDate']}")
            print(f" {COLORS.WHSL}Размер    :  {COLORS.GNSL}{i['torrent']['size']}")
    else:
        print(f" {COLORS.WHSL}По вашему запросу нечего не найдено")


from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True


def blockchain(q):
    br = Firefox(options=opts)
    print(' ------------------------------------')
    br.get(f'https://www.blockchain.com/btc/address/{q}')
    ob_inf = br.find_element_by_xpath('.//*[@class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"]').text
    print(f'{ob_inf}')
    print(' ------------------------------------')
    # br.get(f'https://blockchair.com/search?q={q}')
    # try:
    # if br.find_element_by_xpath('.//*[@class="mb-30"]'):
    # print(f' Данный адресс встречается в следующих крипто-платформах:\n')
    # for elem in br.find_elements_by_xpath('.//*[@class="display-block c-black bgc-white br-8 plr-15 ptb-10 mb-5 hover-highlight"]'):
    # crypto_money = elem.find_element_by_xpath("div[1]").text.split('\n')
    # balance = elem.find_element_by_xpath('div[3]').text.split('\n')
    # print(f'{crypto_money[0]}\t{balance[1]} ({balance[2]})\n')
    # print('------------------------------------')
    # except Exception as er1:
    # print('\n Ошибка обработки запроса. Отправте ошибку разработчику')
    # print(f' ER1 ==>> {er1}\n')
    print('\n ------- Информация о Bitcoin адрессе -------')
    br.get(f'https://blockchair.com/bitcoin/address/{q}')
    time.sleep(5)
    br.find_element_by_xpath('.//*[@class="address-aside__expand-checkmark mr-5 p-relative d-flex ai-center"]').click()
    ad_info = [elem.text for elem in br.find_elements_by_xpath(
        './/*[@class="transaction-costs__values font-p fs-15 medium ls-2 d-flex ai-center fw-wrap "]')]
    print(f' Тип кошелька (формат):\t {ad_info[0]}')
    print(f' Первое изменение кошелька:  ' + ad_info[1].replace("\n", " "))
    print(f' Поледнее изменеие кошелька: ' + ad_info[2].replace("\n", " "))
    print(f' Количество транзакций: \t{ad_info[3]}')
    print(f' Количество выходных данных: {ad_info[4]}')
    print(f' Неизрасходованных выходных данных: {ad_info[5]}')
    bal = [elem.text.replace('\n', ' (') for elem in
           br.find_elements_by_xpath('.//*[@class="account-hash__balance__values"]')]
    # t_bal = br.find_element_by_xpath('.//*[@class="account-hash__balance__values"]').text.replace('\n', ' (')
    print(f' Текущий баланс:   {bal[0]})')
    print(f' Всего получено:   {bal[1]})')
    print(f' Всего отправлено: {bal[2]})')
    print('\n ------- История транзакций (последние 5)-------')
    history_all = br.find_elements_by_xpath('.//*[@class="tr-history__btc-entry-wrap"]')
    for elem in history_all[:5]:
        # print('\n\t*****')
        # print(f' Тип транзакции:  ' + elem.find_element_by_xpath('.//*[@class="tr-history__btc-entry__top__type"]').text)
        # print(f' ID транзакции:   ' + elem.find_element_by_xpath('.//*[@class="hash-sm d-iflex ai-center p-relative grow-10 fs-14 data-v-tooltip"]').get_attribute('data-v-tooltip'))
        # print('                 \t' + elem.get_attribute('href'))
        # print(f' Дата транзакции: ' + elem.find_element_by_xpath('.//*[@class="value-wrapper d-iflex ai-center"]/span/span').text + ' UTC')
        # print(f' Сумма перевода:  ' + elem.find_element_by_xpath('.//*[@class="tr-history__btc-entry__top__amount"]').text.replace('\n', ' (') + ')')
        # print(f' Отправителей:    ' + elem.find_element_by_xpath('.//*[@class="tr-history__btc-entry__bottom__io ml-auto"]/div[1]/span').text)
        # print(f' Получателей:     ' + elem.find_element_by_xpath('.//*[@class="tr-history__btc-entry__bottom__io ml-auto"]/div[2]/span').text)
        print('\n\t*****')
        print(f' Тип транзакции:  ' + elem.find_element_by_xpath('div[1]/div[1]').text)
        print(f' ID транзакции:   ' + elem.find_element_by_xpath('div[2]/div[1]/div[1]/a').text)
        # print('                 \t' + elem.get_attribute('href'))
        print(f' Дата транзакции: ' + elem.find_element_by_xpath('div[1]/div[4]/span/span/span').text + ' UTC')
        print(f' Сумма перевода:  ' + elem.find_element_by_xpath('div[1]/div[3]').text.replace('\n', ' (') + ')')
        print(f' Отправителей:    ' + elem.find_element_by_xpath('div[2]/div[2]/div[1]/span').text)
        print(f' Получателей:     ' + elem.find_element_by_xpath('div[2]/div[2]/div[2]/span').text)
    print(' ------------------------------------')
    print('\n ------- Жалобы на адресс -------\n')
    no_abuse = None
    br.get(f'https://www.bitcoinabuse.com/reports/{q}')
    time.sleep(2)
    try:
        if br.find_elements_by_xpath('.//*[@class="container mb-4"]/table/tbody/tr/td[1]'):
            print(' Дата \t     | Тип жалобы | Описание')
            for elem in br.find_elements_by_xpath('.//*[@class="container mb-4"]/table/tbody/tr'):
                date = elem.find_element_by_xpath('td[1]').text
                abuse_type = elem.find_element_by_xpath('td[2]').text
                description = elem.find_element_by_xpath('td[3]').text
                print(f'{date} |  {abuse_type} \t | {description}')
        else:
            no_abuse = 1
    except Exception as er2:
        print('\n Ошибка обработки запроса. Отправте ошибку разработчику')
        print(f' ER2 ==>> {er2}\n')
    br.get(f'https://cryptscam.com/ru/detail/{q}')
    time.sleep(2)
    try:
        if br.find_elements_by_xpath('.//*[@class="col-md-10 my-1"]'):
            for elem in br.find_elements_by_xpath('.//*[@class="card-body"]'):
                scam_info = [inf.text for inf in elem.find_elements_by_xpath('.//*[@class="col-md-10 my-1"]')]
                print(f'\n Дата\t\t\t{scam_info[0]}')
                print(f' Тип\t\t\t{scam_info[1]}')
                print(f' Мошенник/обидчик\t{scam_info[2]}')
                print(f' Страна\t\t\t{scam_info[3]}')
                print(f' Описание\t\t{scam_info[4]}')
                print(f' Источник\t\t{scam_info[5]}')
                print(f' Адрес сайта\t\t{scam_info[6]}')
        else:
            no_abuse = 1
    except Exception as er3:
        print('\n Ошибка обработки запроса. Отправте ошибку разработчику')
        print(f' ER3 ==>> {er3}\n')
    if no_abuse:
        print(' Жалоб на адресс не найдено')

    br.quit()


def dnsdumpster(domain):
    from grab import Grab
    g = Grab()
    g.setup(timeout=6000, connect_timeout=60)
    g.go('https://dnsdumpster.com/')
    g.doc.set_input_by_xpath('//*[@id="regularInput"]', domain)
    g.submit()
    tables = [i for i in g.doc.select('//*[table]')]
    print(f'\n\n\n{COLORS.WHSL}                ####### DNS Servers #######{COLORS.GNSL}\n')
    for elem in tables[0].select('.//*[td]'):
        dns_server = elem.select('td[1]').text()
        ip_info = elem.select('td[2]/span').text()
        ip = elem.select('td[2]').text().replace(ip_info, '')
        country_prov = elem.select('td[3]/span').text()
        prov = elem.select('td[3]').text().replace(country_prov, '')
        print(f'{dns_server}\t\t{ip} ({ip_info})\t\t{prov} ({country_prov})')
        print(
            f'{COLORS.REDL}____________________________________________________________________________________________________{COLORS.GNSL}\n')
    print(f'\n\n\n{COLORS.WHSL}               ####### MX Records #######{COLORS.GNSL}\n')
    for elem in tables[1].select('.//*[td]')[:5]:  # 5 pervih zapisei
        dns_server = elem.select('td[1]').text()
        ip_info = elem.select('td[2]/span').text()
        ip = elem.select('td[2]').text().replace(ip_info, '')
        country_prov = elem.select('td[3]/span').text()
        prov = elem.select('td[3]').text().replace(country_prov, '')
        print(f'{dns_server}\t\t{ip} ({ip_info})\t\t{prov} ({country_prov})')
        print(
            f'{COLORS.REDL}____________________________________________________________________________________________________{COLORS.GNSL}\n')
    print(f'\n\n\n{COLORS.WHSL}               ####### Host Records (A) #######{COLORS.GNSL}\n')
    for elem in tables[3].select('.//*[td]')[:5]:  # 5 pervih zapisei
        dns_server = elem.select('td[1]').text().split(' ')[0]
        try:
            dns_info_1 = elem.select('td[1]/span[1]').text() + ' ' + elem.select('td[1]/span[2]').text() + ' |'
            dns_info_2 = '| ' + elem.select('td[1]/span[3]').text() + ' ' + elem.select('td[1]/span[4]').text()
        except:
            dns_info_1 = ''
            dns_info_2 = ''
        ip_info = elem.select('td[2]/span').text()
        ip = elem.select('td[2]').text().replace(ip_info, '')
        country_prov = elem.select('td[3]/span').text()
        prov = elem.select('td[3]').text().replace(country_prov, '')
        # print(f'{dns_server}\t\t{ip} ({ip_info})\t\t{prov} ({country_prov})')
        print(f'{dns_server}  ({dns_info_1}{dns_info_2})\t\t{ip} ({ip_info})\t\t{prov} ({country_prov})')
        print(
            f'{COLORS.REDL}____________________________________________________________________________________________________{COLORS.GNSL}\n')
    print(f"\n\n\n{COLORS.WHSL}              ####### TXT Records #######{COLORS.GNSL}\n")
    try:
        txt = tables[2].select('.//*[td]').text()
    except:
        txt = 'Not TXT Records'
    print(f'{txt}\n\n')
    try:
        url_xlsx = 'https://dnsdumpster.com' + g.doc.select('//*[@class="table-responsive"]/div[1]/a[1]').attr('href')
        url_graph = 'https://dnsdumpster.com' + g.doc.select('//*[@class="table-responsive"]/div[1]/a[2]').attr('href')
        url_png = f'https://dnsdumpster.com/static/map/{domain}.png'
    except:
        url_xlsx = 'https://dnsdumpster.com' + g.doc.select('//*[@class="table-responsive"]/div[2]/a[1]').attr('href')
        url_graph = 'https://dnsdumpster.com' + g.doc.select('//*[@class="table-responsive"]/div[2]/a[2]').attr(
            'href')
        url_png = f'https://dnsdumpster.com/static/map/{domain}.png'
    print(f' {COLORS.WHSL}Ссылки для просмотра результата через браузер:\n{COLORS.REDL}')
    print(url_xlsx)
    print(url_graph)
    print(url_png)
    print(
        f'{COLORS.REDL}____________________________________________________________________________________________________{COLORS.GNSL}\n')
    download = input(f'\n{COLORS.WHSL} Сохранить результат в папку module/db?{COLORS.REDL}\ty/n:{COLORS.GNSL}')
    print(
        f'{COLORS.REDL}____________________________________________________________________________________________________{COLORS.GNSL}\n')
    if download == 'y':
        g.go(url_xlsx)
        if g.doc.code == 200:
            g.doc.save(f'module/db/{domain}.xlsx')
            print(f' {COLORS.WHSL}Результат в виде .XLSX сохранен в module/db/{domain}.xlsx {COLORS.GNSL}')
        else:
            print(f' {COLORS.WHSL}Сервер не вернул результат. Перейдите по ссылке вручную.')
            return
        # create HTMl-graph
        # g.go(url_graph)
        # if g.doc.code == 200:
        #     g.doc.save(f'module/db/{domain}.html')
        #     print(f' {COLORS.WHSL}Результат в виде ГРАФА сохранен в module/db/{domain}.html')
        html = '<html><body><iframe frameborder="0" src="' + url_graph + '"></iframe><style type="text/css">iframe{position:absolute;top:0px;left:0px;width:100%;height:100%;}</style></body></html>'
        f = open(f'module/db/{domain}.html', 'w')
        f.write(html)
        f.close()

        print(f' {COLORS.WHSL}Результат в виде ГРАФА сохранен в module/db/{domain}.html')
        g.go(url_png)
        if g.doc.code == 200:
            g.doc.save(f'module/db/{domain}.png')
            print(f' {COLORS.WHSL}Результат в виде КАРТЫ сохранен в module/db/{domain}.png')
    else:
        print(f' {COLORS.WHSL}Выход')
        # print('Exit')
