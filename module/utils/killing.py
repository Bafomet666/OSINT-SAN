
from module.utils import COLORS
from pyngrok import ngrok
import subprocess
import os
import time


def kill():
    ngrok.kill()
    os.system('rm -rf __pycache__')
    os.system('rm -rf core/__pycache__')
    os.system('rm -rf module/__pycache__')
    os.system('rm -rf module/utils/__pycache__')
    os.system('rm -rf module/maigret/__pycache__')
    print(f' {COLORS.FIOL}Благодарим вас за использование !!!{COLORS.WHSL} Вы прекрасны.\n')
    time.sleep(0.5)
    subprocess.call('pkill -9 php', shell=True)
    subprocess.call('pkill -9 -f osintsan.py', shell=True)


def restart():
    ngrok.kill()
    os.system('pkill -9 php')
    os.system('rm -rf __pycache__')
    os.system('rm -rf core/__pycache__')
    os.system('rm -rf module/__pycache__')
    os.system('rm -rf module/utils/__pycache__')
    os.system('rm -rf module/maigret/__pycache__')
    subprocess.call("adb disconnect >> /dev/null", shell=True)
    subprocess.call("adb kill-server >> /dev/null", shell=True)
    print(f'{COLORS.REDL} Авторизация прошла успешно\n')
    print(f'{COLORS.FIOL} Перезапуск прошел успешно, \n выключены дополнительные процессы python клиента osint-sany')
