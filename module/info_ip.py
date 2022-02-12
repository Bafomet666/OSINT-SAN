# Developer by Bafomet
# -*- coding: utf-8 -*-

import shodan
import time
import json
import requests
import random
from osintsan import api
from module.utils import COLORS

shodan_api = api['Shodan']


def blockchain(q):
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.options import Options

    opts = Options()
    opts.headless = True
    br = Firefox(options=opts)
    print(' ------------------------------------')
    br.get(f'https://www.blockchain.com/btc/address/{q}')
    ob_inf = br.find_element_by_xpath('.//*[@class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"]').text
    print(f'{ob_inf}')
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
