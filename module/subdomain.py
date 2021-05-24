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

active_subdomains = []


class subzone:
	def __init__(self):
		pass


	def get(self,args):
		#parse host from scheme, to use for certificate transparency abuse
		try:
			host = urllib3.util.url.parse_url(args).host
		except Exception as e:
			print(f'Invalid - Domain, try again...')
			sys.exit(1)

		#request json data to get list of registered subdomains with cert trans records
		subdomains = []
		try:
			r = requests.get(f'https://crt.sh/?q=%.{host}&output=json')
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
	
		#check registered subdomains to see if active or not
		global active_subdomains

		for sub in subdomains:
			try:
				sub = socket.gethostbyname_ex(sub)
				active_subdomains.append(sub)
			except:
				pass
		number_all = len(subdomains)
		number_active = len(active_subdomains)

		Style.RESET_ALL

		try:
			print('\n',Fore.GREEN+'''{!} There are %s %s %s''' %
				(Fore.RED+Back.BLACK+str(number_all), Fore.RED+Back.BLACK+'REGISTERED', Fore.GREEN+'subdomains for this domain.'))
			time.sleep(2)

			index = Fore.GREEN+Back.BLACK+str('INDEX:green')
			sub_red = Fore.RED+Back.BLACK+str('SUBDOMAIN:red')
			line = Fore.CYAN+Back.BLACK+str('*****************************')
			print('\n%s\n%s %s\n%s\n' % (line, index, sub_red, line))
			time.sleep(1.3)

			for index, sub in enumerate(subdomains):
				print(Fore.GREEN+str(index),Fore.RED+str(sub))

			print('\n',Fore.GREEN+'''{!} There are %s %s %s''' %
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
				print(Fore.GREEN+str(index),(sub[0]), Fore.RED+Back.BLACK+str(sub[1]), Fore.BLUE+Back.BLACK+str(sub[2]))

		except Exception as e:
			print(f'active_subdomains//Error: {e}')
			pass




subzone = subzone()
