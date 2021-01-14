#imports
from colorama import init, Fore, Back, Style
import requests
import json
import argparse
import socket
import time
import urllib3
import subprocess
import os
import sys
import time

init(autoreset=True)

active_subdomains = []
nameservers = []

class Abuse_certificate_transparency:
	def __init__(self, domain, output):
		self.domain = domain
		self.output = output


	def parse_url(self):
		#parse host from scheme, to use for certificate transparency abuse
		try:
			host = urllib3.util.url.parse_url(self.domain).host
		except Exception as e:
			print(f'Invalid - Domain, try again...')
			sys.exit(1)
		return host

	def request_json(self):
		#request json data to get list of registered subdomains with cert trans records
		subdomains = []
		try:
			r = requests.get(f'https://crt.sh/?q=%.{abuse.parse_url()}&output=json')
			#r = requests.get('https://crt.sh/?q=%.facebook.com&output=json')
			if r.status_code != 200:
				print('{!} host status-code: %s\n ~ unable to access records using this abuse certificate transparency method' % (r.status_code))
			else:
				try:
					json_data = json.loads(r.text)
					for sub in (json_data):
						subdomains.append(sub['name_value'])
				except Exception as e:
					print(f'json_data:Error {e}')
					pass
		except Exception as e:
			print(f'request_json//Error: {e}')
			pass
		return subdomains

	def active_subs(self):
		#check registered subdomains to see if active or not
		global active_subdomains

		for sub in abuse.request_json():
			try:
				sub = socket.gethostbyname_ex(sub)
				if sub in active_subdomains:
					pass
				else:
					active_subdomains.append(sub)
			except:
				continue
		number_all = len(abuse.request_json())
		number_active = len(active_subdomains)

		Style.RESET_ALL

		try:
			print('\n',Fore.GREEN+'''\n\n{!} There are %s %s %s''' %
				(Fore.RED+Back.BLACK+str(number_all), Fore.RED+Back.BLACK+'REGISTERED', Fore.GREEN+'subdomains for this domain.'))
			time.sleep(2)

			index = Fore.GREEN+Back.BLACK+str('INDEX:green')
			sub_red = Fore.RED+Back.BLACK+str('SUBDOMAIN:red')
			line = Fore.CYAN+Back.BLACK+str('*****************************')
			print('\n%s\n%s %s\n%s\n' % (line, index, sub_red, line))
			time.sleep(1.3)

			for index, sub in enumerate(abuse.request_json()):
				print(Fore.GREEN+str(index+1),Fore.RED+str(sub))

			print('\n',Fore.GREEN+'''\n\n{!} There are %s %s %s''' %
				(Fore.RED+Back.BLACK+str(number_active), Fore.RED+Back.BLACK+'ACTIVE', Fore.GREEN+'subdomains for this domain.'))
			time.sleep(2)

			index = Fore.GREEN+Back.BLACK+str('INDEX:green')
			dns_white = Fore.WHITE+Back.BLACK+str('DNS SERVER:white')
			sub_red = Fore.RED+Back.BLACK+str('SUBDOMAIN:red')
			ip_yell = Fore.BLUE+Back.BLACK+str('IP_ADDR:blue')
			line = Fore.CYAN+Back.BLACK+str('************************************************************')
			print('\n%s\n%s %s %s %s\n%s\n' % (line, index, dns_white, sub_red, ip_yell, line))
			time.sleep(1.3)

			for index, sub in enumerate(active_subdomains):
				print(Fore.GREEN+str(index+1), Fore.WHITE+Back.BLACK+str(sub[0]), Fore.RED+Back.BLACK+str(sub[1]), Fore.BLUE+Back.BLACK+str(sub[2]))

		except Exception as e:
			print(f'active_subdomains//Error: {e}')
			pass

		return active_subdomains


	def write_file(self,):
		#write registerd subdomains and active subdomains to file
		global active_subdomains
		try:
			if self.output is not None:
				reg = 'REGISTERED_'+self.output
				active = 'ACTIVE_'+self.output
				with open(reg,'w') as r:
					for index, sub in enumerate(abuse.request_json()):
						text = f'{index} {sub}\n'
						r.write(text)
				with open(active,'w') as a:
					for index, sub in enumerate(active_subdomains):
						text = f'{index} {sub}\n'
						a.write(text)
		except Exception as e:
			print(f'write_file//Error: {e}')
			pass

class Dns_zone_transfer:
	def __init__(self, output):
		self.domain = abuse.parse_url()
		self.output = output

	def nslookup(self):
		global nameservers
		#nslookup to find nameservers of target domain
		dns_white = Fore.RED+Back.BLACK+str('Dns records')
		sec_bit = Fore.GREEN+Back.BLACK+str('for this domain.\n')
		print(Fore.GREEN+Back.BLACK+str('\n\n\n{!} %s %s' % (dns_white, sec_bit)))
		line = Fore.CYAN+Back.BLACK+str('************************************************************')
		records = Fore.GREEN+Back.BLACK+str('DNS RECORDS:green')
		print('%s\n%s\n%s\n' % (line, records, line))
		try:
			with open('nslookup.txt','w') as output_vale:
				cmd = subprocess.call(f'nslookup -type=ns {self.domain}', stdout=output_vale)
			with open('nslookup.txt','r') as ns2:
				for line in ns2.readlines():
					if 'nameserver' in line:
						line = line.split(' ')[2]
						nameservers.append(line)

			os.remove('nslookup.txt')
			#print(nameservers)
		except Exception as e:
			#print(e)
			pass
		return nameservers

	def dns_records(self):
		global nameservers
		#zone transfer - to get dns records if dns server is not configured properly
		count = 0
		try:
			for ns in nameservers:                                                 
                                                      
				with open('gogo.txt','w') as go:
					go.write(f'nslookup\nset type=all\nserver {ns}\nls -d {abuse.parse_url()}\n.\n')

				if self.output is not None:
					filename = 'DNS_RECORDS_%s' % (self.output)
					if count == 0:
						with open(filename,'w') as fp:
							fp.write('**********DNS RECORDS**********\n\n')
							with open('gogo.txt','r') as go:
								cmd = subprocess.call('cmd.exe', stdin=go, stdout=fp)
							count +=1
					else:
						with open(filename,'a') as write_here:
							with open('gogo.txt','r') as go:
								cmd = subprocess.call('cmd.exe', stdin=go, stdout=write_here)
				else:
					with open('gogo.txt','r') as fp:
						cmd = subprocess.call('cmd.exe', stdin=fp)
					fp.close()
		except Exception as e:
			print(e)

		try:
			os.remove('gogo.txt')
		except:
			pass

		try:
			with open(filename,'r') as rd:
				for line in rd.readlines():
					print(line)
		except:
			pass

if __name__=='__main__':
    
    while True:
        try:
            #l3e86
            domain = input('Укажите url > ')
            output = input('Укажите имя выходного файла > ')
            print('  Подождите идет сбор информации, время ожидания одна минута')
            time.sleep(1)
            ############
            
	        # Abuse certificate authority to get all and active subdomains of a domain
            abuse = Abuse_certificate_transparency(domain, output)
            abuse.parse_url()
            abuse.request_json()
            abuse.active_subs()
            abuse.write_file()

            # Dns zone transfer to see if any information is leaking
            zone = Dns_zone_transfer(output)
            zone.nslookup()
            zone.dns_records()
            
            print('Что-бы использовать снова нажмите Enter, выйти в главное меню 99, для выхода 0')
            try:
                cheak_input = input('> ')
                if cheak_input == '99':
                    subprocess.call('python3 osintsan.py', shell=True)
                elif cheak_input == 0:
                    sys.exit()
                    print('[!] Пока')
                else:
                    pass
                    
            except KeyboardInterrupt:
                sys.exit()
	        
        except KeyboardInterrupt:

            print(':> SubZone Completed')
            sys.exit(0)
