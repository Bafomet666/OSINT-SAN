# by bafomet
# imports
from colorama import init, Fore, Back, Style
import requests
import json
import socket
import urllib3
import subprocess
import io
import time

R = '\033[31m'  # Red
N = '\033[1;37m'  # White
G = '\033[32m'  # Green
O = '\033[0;33m'  # Orange
B = '\033[1;34m'  # Blue
P = '\033[1;35m'  # Purple

init(autoreset=True)


def get_host(domain):
    return urllib3.util.url.parse_url(domain).host


class AbuseCertificateTransparency:

    def __init__(self, domain, output):
        self.domain = domain
        self.output = output

    def run(self):
        subdomains = self.request_json()
        active_subdomains = self.active_subs(subdomains)
        self.write_file(subdomains, active_subdomains)

    def request_json(self):
        #  request json data to get list of registered subdomains with cert trans records
        r = requests.get(
            "https://crt.sh",
            params={
                "q": f"%.{self.domain}",
                "output": "json",
            }
        )
        if r.status_code != 200:
            print(f'[!] host status-code: {r.status_code}')
            print('~ unable to access records using this abuse certificate transparency method')
            return

        json_data = json.loads(r.text)
        subdomains = []
        for sub in json_data:
            subdomains.append(sub['name_value'])

        return subdomains

    def active_subs(self, subdomains):
        # check registered subdomains to see if active or not

        active_subdomains = []
        for sub in subdomains:
            try:
                sub = socket.gethostbyname_ex(sub)
            except:
                continue
            else:
                if sub not in active_subdomains:
                    active_subdomains.append(sub)

        number_all = len(subdomains)
        number_active = len(active_subdomains)

        Style.RESET_ALL

        try:
            print()
            print(
                f"{Fore.GREEN}\n\n"
                f"[!] There are {Fore.RED + Back.BLACK + str(number_all)}"
                f" {Fore.RED + Back.BLACK + '  REGISTERED'}"
                f" {Fore.GREEN + '  subdomains for this domain.'}"
            )
            time.sleep(2)

            index = Fore.GREEN + Back.BLACK + str('  INDEX:green')
            sub_red = Fore.RED + Back.BLACK + str('  SUBDOMAIN:red')
            line = Fore.CYAN + Back.BLACK + str('*****************************')
            print()
            print(line)
            print(f"{index} {sub_red}")
            print(line)
            time.sleep(1.3)

            for index, sub in enumerate(subdomains):
                print(Fore.GREEN + str(index + 1), Fore.RED + str(sub))

            print()
            print(
                f"{Fore.GREEN}\n\n[1] There are "
                f"{Fore.RED + Back.BLACK + str(number_active)} "
                f"{Fore.RED + Back.BLACK + 'ACTIVE'} "
                f"{Fore.GREEN + '  subdomains for this domain.'}"
            )

            time.sleep(2)

            index = Fore.GREEN + Back.BLACK + str('  INDEX:green')
            dns_white = Fore.WHITE + Back.BLACK + str('  DNS SERVER:white')
            sub_red = Fore.RED + Back.BLACK + str('  SUBDOMAIN:red')
            ip_yell = Fore.BLUE + Back.BLACK + str('  IP_ADDR:blue')
            line = Fore.CYAN + Back.BLACK + str(
                '************************************************************')

            print()
            print(line)
            print(f"{index} {dns_white} {sub_red} {ip_yell}")
            print(line)

            time.sleep(1.3)

            for index, sub in enumerate(active_subdomains):
                print(
                    Fore.GREEN + str(index + 1),
                    Fore.WHITE + Back.BLACK + str(sub[0]),
                    Fore.RED + Back.BLACK + str(sub[1]),
                    Fore.BLUE + Back.BLACK + str(sub[2]),
                )

        except Exception as e:
            print(f'active_subdomains//Error: {e}')
            pass

        return active_subdomains

    def write_file(self, subdomains, active_subdomains):
        # write registerd subdomains and active subdomains to file

        try:
            if self.output is not None:
                reg = '  REGISTERED_' + self.output
                active = '  ACTIVE_' + self.output

                with open(reg, 'w') as r:
                    for index, sub in enumerate(subdomains):
                        r.write(f'{index} {sub}\n')

                with open(active, 'w') as a:
                    for index, sub in enumerate(active_subdomains):
                        a.write(f'{index} {sub}\n')

        except Exception as e:
            print(f'write_file//Error: {e}')


class DnsZoneTransfer:
    def __init__(self, domain, output):
        self.domain = domain
        self.output = output

    def run(self):
        nameservers = self.nslookup()
        self.dns_records(nameservers)

    def nslookup(self):
        # nslookup to find nameservers of target domain
        dns_white = Fore.RED + Back.BLACK + str('Dns records')
        sec_bit = Fore.GREEN + Back.BLACK + str('for this domain.')
        print(Fore.GREEN + Back.BLACK + str(f'\n\n\n[!] {dns_white} {sec_bit}'))
        print()

        line = Fore.CYAN + Back.BLACK + str(
            '************************************************************')
        records = Fore.GREEN + Back.BLACK + str('DNS RECORDS:green')
        print(line)
        print(records)
        print(line)

        result = subprocess.check_output(["nslookup", "-type=ns", self.domain]).decode()
        nameservers = []
        for line in result.splitlines():
            nameserver = line.split(' ')[2]
            nameservers.append(nameserver)

        return nameservers

    def dns_records(self, nameservers):
        # zone transfer - to get dns records if dns server is not configured properly
        filename = f'DNS_RECORDS_{self.output}'
        command = 'nslookup\n' \
                  'set type=all\n' \
                  'server\n' \
                  '{ns}\n' \
                  f'ls -d {self.domain}\n' \
                  f'.\n'
        with open(filename, 'w') as fp:
            fp.write('**********DNS RECORDS**********\n\n')

            for ns in nameservers:

                command_ = command.format(ns=ns)

                if self.output is not None:
                    subprocess.Popen(
                        ['cmd.exe'],
                        stdin=subprocess.PIPE,
                        stdout=fp,
                    ).communicate(command_.encode())
                else:
                    subprocess.Popen(
                        ['cmd.exe'],
                        stdin=subprocess.PIPE,
                    ).communicate(command_.encode())

        try:
            with open(filename, 'r') as rd:
                for line in rd.readlines():
                    print(line)
        except:
            pass


def subzone():
    while True:
        try:
            # l3e86
            print()
            url = input(f"{B} Вводите url : ")
            print()
            output = input(f"{G} Укажите имя выходного файла : ")
            print()
            print(f"{R} Подождите идет сбор информации, время ожидания одна минута")
            print()
            print(f"{R} Данные будут сохранены в папке module.")
            time.sleep(1)
            ############

            # Abuse certificate authority to get all and active subdomains of a domain
            domain = get_host(url)
            abuse = AbuseCertificateTransparency(domain, output)
            abuse.run()

            # Dns zone transfer to see if any information is leaking
            zone = DnsZoneTransfer(domain, output)
            zone.run()

            print(f"{R} Для выхода введи 99")
            try:
                check_input = input('> ')

                if check_input == '99':
                    return

                elif len(check_input) == 0:
                    print('[!] Пока')
                    return

                else:
                    pass

            except KeyboardInterrupt:
                return

        except KeyboardInterrupt:

            print(':> SubZone Completed')
            return


if __name__ == '__main__':
    subzone()
