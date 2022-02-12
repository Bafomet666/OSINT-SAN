# Легкий и понятный код по установке зависимостей, сделано для новичков.
from module.utils.banner import show_banner
import subprocess


def driver(option):
    import webbrowser
    import os
    if option == '1':
        os.system('sudo apt install libcurl4-gnutls-dev librtmp-dev')
        os.system('sudo apt-get install libcurl4-gnutls-dev librtmp-dev')
        os.system('pip3 install setuptools')
        os.system('pip3 install pycurl')
        os.system('pip3 install grab')
        print(' \n Установка прошла успешно\n')

    elif option == '2':
        os.system(
            'wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz')
        os.system('sudo tar -xvzf geckodriver-v0.30.0-linux64.tar.gz')
        os.system('sudo chmod +x /usr/local/bin/geckodriver')
        os.system('sudo mv geckodriver /usr/local/bin/geckodriver')
        os.system('sudo chown root:root /usr/local/bin/geckodriver')

    elif option == '3':
        os.system('sudo pip3 install -r requirements.txt')
        print(' \n Установка прошла успешно\n')

    elif option == '4':
        print(f' Установка и проверка зависимостей')
        subprocess.call(f'sudo apt-get install android-tools-adb android-tools-fastboot', shell=True)

    elif option == '5':
        urls = [
            "https://t.me/satana666mx",
        ]
        for url in urls:
            webbrowser.open(url)
        print(f"\n Сайты открыты")

    elif option == '6':
        page_2 = f''' Друг я пока еще не проработал эту функцию в автомат
                      Перейди по ссылкам там гайд
                      
                      https://tecadmin.net/setup-selenium-with-chromedriver-on-debian/
                      https://bytetell.com/123/
                      https://losst.ru/ustanovka-selenium-v-linux '''
        print(page_2)

    elif option == '7':
        os.system('sudo apt remove fonts-noto-color-emoji')
        os.system('sudo apt install fonts-noto-color-emoji')

        print(' Успешно')

    elif option == '99':
        show_banner(clear=True)
