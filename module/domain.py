# OSINT-SAN
import requests
from module.utils.ban import menu
from module.utils.banner import show_banner
from module.utils import COLORS
from osintsan import api

virustotal_api = api['virustotal_api']
cms_detect_api = api['cms_detect_api']


def run():
    try:
        print(menu)
        choice = input(
            f"{COLORS.REDL} └──>{COLORS.GNSL}  Выберите опцию {COLORS.GNSL}[ {COLORS.REDL}main_menu{COLORS.GNSL} ]{COLORS.GNSL}: ")

        if choice == '1':
            show_banner(clear=True)
            from module.info_ip import dnsdumpster
            domain = input(f'{COLORS.REDL} └──>{COLORS.WHSL} Введите домен для поиска информации:{COLORS.GNSL} ')
            dnsdumpster(domain)

        elif choice == '2':
            from urllib.parse import urlparse
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: http://google.com \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n [ + ] Headers :\n')
            response = requests.get(target, verify=True, timeout=10)
            for k, v in response.headers.items():
                print(f' [ + ] {k} : {v}')
            run()

        elif choice == '3':
            show_banner(clear=True)
            dnslookup = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            dnslookup = 'https://api.hackertarget.com/dnslookup/?q=' + dnslookup
            info = requests.get(dnslookup)
            print(info.text)
            print(info.text)
            run()

        elif choice == '4':
            show_banner(clear=True)
            revers = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            reversedns = 'https://api.hackertarget.com/reversedns/?q=' + revers
            info = requests.get(reversedns)
            print(info.text)
            run()

        elif choice == '5':
            from grab import Grab
            from selenium.webdriver import Firefox
            from selenium.webdriver.firefox.options import Options
            opts = Options()
            opts.headless = True
            br = Firefox(options=opts)
            show_banner(clear=True)
            print(f' {COLORS.WHSL}Примеры ввода запроса: {COLORS.GNSL}google.com, pornohub.com, ruvds.com \n')
            inp = input(f'{COLORS.REDL} ──> {COLORS.GNSL}Введите domain: {COLORS.WHSL}')
            print(f"\n {COLORS.GNSL}Ожидайте пока закончится сбор информации.{COLORS.WHSL} \n")
            br.get(f'https://viewdns.info/reversewhois/?q={inp}')
            try:
                all_list = br.find_elements_by_xpath('/html/body/font/table[2]/tbody/tr[3]/td/font/table/tbody/tr')
                if not all_list:
                    br.quit()
                    print(f' Ничего не найдено по вашему запросу')
                else:
                    for elem in all_list:
                        domain, date, registrar = elem.find_elements_by_xpath('td')
                        print(f' {domain.text}\t\t{date.text}\t\t{registrar.text}')
                        print(f" {COLORS.REDL}={COLORS.WHSL}" * 70)
                        print()
                    br.quit()
            except:
                br.quit()

        elif choice == '6':
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: google.com \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            request_urls = "https://api.hackertarget.com/findshareddns/?q="
            request_url = request_urls
            url = request_url + target
            request = requests.get(url)
            print(request.text)
            run()

        elif choice == '7':
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: google.com, vsechastikino.ru \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            request_urls = "https://api.hackertarget.com/zonetransfer/?q="
            request_url = request_urls
            url = request_url + target
            request = requests.get(url)
            print(request.text)
            run()

        elif choice == '8':
            import whois
            print(' Пример ввода: google.com \n')
            data = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите доменное имя: ")
            test = whois.whois(data)
            show_banner(clear=True)
            print(test)

        elif choice == '9':
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: google.com \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            request_urls = "https://api.hackertarget.com/geoip/?q="
            request_url = request_urls
            url = request_url + target
            request = requests.get(url)
            print(request.text)
            run()

        elif choice == '10':
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: google.com \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            request_urls = "https://api.hackertarget.com/reverseiplookup/?q="
            request_url = request_urls
            url = request_url + target
            request = requests.get(url)
            print(request.text)
            run()

        elif choice == '11':
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: http://google.com \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            request_urls = "https://api.hackertarget.com/nmap/?q="
            request_url = request_urls
            url = request_url + target
            request = requests.get(url)
            print(request.text)
            run()

        elif choice == '12':
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: http://google.com \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            request_urls = "https://api.hackertarget.com/subnetcalc/?q="
            request_url = request_urls
            url = request_url + target
            request = requests.get(url)
            print(request.text)
            run()

        elif choice == '13':
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: http://google.com \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            request_urls = "https://api.hackertarget.com/httpheaders/?q="
            request_url = request_urls
            url = request_url + target
            request = requests.get(url)
            print(request.text)
            run()

        elif choice == '14':
            show_banner(clear=True)
            print(f'\n Пример ввода ссылки: http://google.com \n')
            target = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print('\n')
            request_urls = "https://api.hackertarget.com/pagelinks/?q="
            request_url = request_urls
            url = request_url + target
            request = requests.get(url)
            print(request.text)
            run()

        elif choice == '15':
            show_banner(clear=True)
            host = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            print(f'\n{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Получение субдоменов цели...\n')
            if not virustotal_api:
                print(
                    f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Проблемы с ключом api, напишите разработчикам !")
                return
            url = 'https://www.virustotal.com/vtapi/v2/domain/report'

            params = {
                'apikey': virustotal_api,
                'domain': host,
            }
            response = requests.get(url, params=params)

            subdomains = response.json()
            for x in subdomains['subdomains']:
                print(x)

            run()

        elif choice == '16':
            requests.packages.urllib3.disable_warnings()
            show_banner(clear=True)
            domain = input(f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Введите address: ")
            if not cms_detect_api:
                print(
                    f"{COLORS.GNSL} [ {COLORS.REDL}+{COLORS.GNSL} ] {COLORS.WHSL} Проблемы с ключом api, напишите разработчикам !")
                return
            payload = {'key': cms_detect_api, 'url': domain}
            cms_url = "https://whatcms.org/APIEndpoint/Detect"
            response = requests.get(cms_url, params=payload)
            cms_data = response.json()
            cms_info = cms_data['result']
            if cms_info['code'] == 200:
                print(f' Detected CMS     : {cms_info["name"]}')
                print(f' Detected Version : {cms_info["version"]}')
                print(f' Confidence       : {cms_info["confidence"]}')
            else:
                print(cms_info['msg'])
                print(f' Detected CMS     : {cms_info["name"]}')
                print(f' Detected Version : {cms_info["version"]}')

            run()

        elif choice == '0':
            import os
            print(f' {COLORS.GNSL}Благодарим вас за использование !!! Вы прекрасны.\n')
            os.system('pkill -9 -f osintsan.py')
            exit()

        elif choice == '99':
            show_banner(clear=True)
            return

    except KeyboardInterrupt:
        print("\nAborted!")
        exit()
