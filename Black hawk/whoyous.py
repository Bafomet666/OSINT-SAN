import requests
import sys
from datetime import datetime

def whois_more(IP):
    result = requests.get('http://api.hackertarget.com/whois/?q=' + IP).text
    print('\n'+ result + '\n')
    
    now = datetime.now()
    data_time = "{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute)
    
    with open('resalt.txt', 'a') as file:
        file.write('[eq')
        #file.write('\n' + '-'*30 + '\n\n' + data_time + '\n\n' + result + '\n')

    
while True:
    try:
        ip_input = input('Укажите IP-адрес > ')
        whois_more(ip_input)
    except KeyboardInterrupt:
        print('Нажмите 99 что-бы выйти в меню или Enter что-бы выйти\n')
        try:
            cheak_input = input('> ')
            if cheak_input == '99':
                subprocess.call('python3 errorlist.py', shell=True)                
            else:
                print('[!] Bye')
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()  
