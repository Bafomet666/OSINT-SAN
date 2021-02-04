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
        print("")
        user_name = input(REDL + " └──>" + WHSL + " Жду от тебя ввод username instagram "+GNSL+"[ "+REDL + "main_menu" + GNSL + " ]"+ENDL + " :")
        print("")
        input(GNSL+" [ "+REDL + "Напоминание" + GNSL + " ]"+ WHSL +" Если захочешь выйти, введи 99. Нажми enter что бы продолжить" +ENDL + " :")
        if user_name == '99':
            os.system("cd ..;python3 osintsan.py")
            break        
        elif user_name == '':
            print('  [ - ] некоректный ввод username')          
            
        else:
            api.user_info(user_name)
              
    except KeyboardInterrupt:
        print('\nпока!')
        break

