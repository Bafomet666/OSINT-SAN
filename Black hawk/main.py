import api
import subprocess
#By bafomet
#By I3e86
# Set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

while True:
    try:
        user_name = input(REDL + "└──>" + WHSL + "Я жду от тебя ввод username instagram"+GNSL+"[ "+REDL + "main_menu" + GNSL + " ]"+ENDL + " :")
        input(GNSL+"[ "+REDL + "Напоминание" + GNSL + " ]"+ WHSL +" Если захочешь выйти или очиcтить нажми 99. Жми enter давай" +ENDL + " :")
        if user_name == '99':
            subprocess.call("python3 errorlist.py", shell=True)
            break        
        elif user_name == '':
            print('[ - ] некоректный ввод username')          
            
        else:
            api.user_info(user_name)
              
    except KeyboardInterrupt:
        print('\nпока!')
        break

