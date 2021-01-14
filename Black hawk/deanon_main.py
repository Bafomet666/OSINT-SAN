import sys
import subprocess

def main():
    while True:
        try:
            print('\n[*] Выбери опцию\n')
            #эквевалент -p
            print('[1] Парсинг железа')
            #эквевалент -с
            print('[2] Крашнуть ngrok противника')
            #эквевалент -l
            print('[3] Отследить гео-локацию')
            
            print('[4] Выйти с перезапуском.')
            
            #запрос у пользователя на ввод операции            
            user_input = input('\n--> ')
            
            try:
                #запрос урла, проверка на пустую строку
                #и если она пустая то возвращаемся в главное меню
                #можно попробовать к вводу урла, но я и так проебал пол дня, весь мозг выстраивая эту ахуенную конструкцию, но если попросишь перепишу
                url = input('\n[!] Укажите URL: ')
                if url == '' or url == ' ':
                    print('\n[-] Неверное значение')
                    
                #если введенна ссылка (так-же думаю стоит сделать проверку на валидность
                #ссылки, но это уже в твоем коде, наверно, башка дымит пыш-пыш)
                #то в зависимости от того какая операция была выполнена, идет отработка
                #модуля deanon_mod.py в который передаются значения урла и тайминг(или
                #что это),в случае если выбрана третья опция
                else:
                    if user_input == '1':
                        subprocess.check_call(['python3', 'deanon_mod.py', '-p', url])
                        
                    elif user_input == '2':
                        subprocess.call(['python3', 'deanon_mod.py', '-c', url])
                    
                    elif user_input == '3':
                        time = input('Укажите задержку в минутах по умолчанию 180минут: ')
                        
                    elif user_input == '4':
                        subprocess.check_call(['python3', 'osintsan.py',])
                        
                        #условие где переменная time(тайминг) 
                        #инициализируется дефолтным значением
                        #при условии пустой строки
                        if time == '' or time == ' ':
                            time = 10800 
                        else:
                            time = int(time) * 60
                        
                        subprocess.check_call(['python3', 'deanon_mod.py', '-l', str(time), url])
            
            #обработчик ошибок тут все ясно            
            except KeyboardInterrupt:
                choice_exit = input('\n[?] Что-бы вернутся в меню нажмите 0, что-бы закончить работу нажмите Enter клавишу\n')
                if choice_exit == '0':
                    pass
                else:
                    sys.exit()  
        
        #еще один, да так нужно!!!! я художник я так вижу!!!                
        except KeyboardInterrupt:
            print('\n[!] пока\n')
            sys.exit()
                          
main()
