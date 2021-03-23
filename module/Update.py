import os
import re
import sys
from requests import get
import time as t
from module.utils.banner import show_banner

if sys.version_info[0] > 2:
    from module.update_log import changes

else:
    from update_log import changes

def update():
    print('\n Проверка обновлений...')
    latestCommit = get('https://raw.githubusercontent.com/Bafomet666/OSINT-SAN/main/core/update_log.py').text

    if changes not in latestCommit:
        changelog = re.search(r"changes = '''(.*?)'''", latestCommit)
        changelog = changelog.group(1).split(';')
        print('\n Доступна новая версия OSINT-SAN.')
        print('\n Изменения:\n')
        for change in changelog:
            print(' Их очень много, качай уже')

        currentPath = os.getcwd().split('/') 
        folder = currentPath[-1]
        path = '/'.join(currentPath)

        if sys.version_info[0] > 2:
            choice = input('\n Обновить сейчас ? [Y/n] ')

        else:
            choice = raw_input('\n Вы хотели бы обновить? [Y/n] ')

        if choice == 'n':
            print('\n Ну и пошел в жопу')
            t.sleep(6)
            show_banner(clear=True)
            
        if choice == 'y':
            print('\n Обновление OSINT-SAN. Ожидайте.')
            os.system('git clone --quiet https://github.com/Bafomet666/OSINT-SAN %s' % (folder))
            os.system('cp -r %s/%s/* %s && rm -r %s/%s/ 2>/dev/null' % (path, folder, path, path, folder))
            print('\n Успешно обновленно!')
            return
        else:
            print('\n Обновление отменено!')

    else:
        print('\n OSINT-SAN Полностью обновлен.')
