import requests
from datetime import datetime


def whois_more(IP):
    result = requests.get('http://api.hackertarget.com/whois/', params={"q": IP}).text
    print(f'\n{result}\n')
    if "API count exceeded" in result:
        return
    
    now = datetime.now()
    data_time = "{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute)
    
    with open('resalt.txt', 'a') as file:
        file.write('[eq')
        file.write('\n')
        file.write("-"*30)
        file.write("\n\n")
        file.write(data_time)
        file.write("\n\n")
        file.write(result)
        file.write("\n")


def whois_menu():
    while True:
        try:
            ip_input = input('Укажите IP-адрес > ')
            whois_more(ip_input)
        except KeyboardInterrupt:
            print('Нажмите 99 что-бы выйти в меню или Enter что-бы продолжить\n')
            try:
                cheak_input = input('> ')
            except KeyboardInterrupt:
                return

            if cheak_input == '99':
                return
            else:
                continue


if __name__ == '__main__':
    whois_menu()
