#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import subprocess
import os
import sys
import readline
#set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'
os.system("printf '\033]2;OSINT Wiki\a'")
os.system('clear')
page_1 = '''{1}

                                  /$$ /$$       /$$                           /$$ /$$                                     /$$             /$$    
                                 |__/| $$      |__/                          | $$|__/                                    |__/            | $$    
                    /$$  /$$  /$$ /$$| $$   /$$ /$$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$         /$$$$$$   /$$$$$$$ /$$ /$$$$$$$  /$$$$$$  
                   | $$ | $$ | $$| $$| $$  /$$/| $$ /$$__  $$ /$$__  $$ /$$__  $$| $$ |____  $$       /$$__  $$ /$$_____/| $$| $$__  $$|_  $$_/  
                   | $$ | $$ | $$| $$| $$$$$$/ | $$| $$  \ $$| $$$$$$$$| $$  | $$| $$  /$$$$$$$      | $$  \ $$|  $$$$$$ | $$| $$  \ $$  | $$    
                   | $$ | $$ | $$| $$| $$_  $$ | $$| $$  | $$| $$_____/| $$  | $$| $$ /$$__  $$      | $$  | $$ \____  $$| $$| $$  | $$  | $$ /$$
                   |  $$$$$/$$$$/| $$| $$ \  $$| $$| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$      |  $$$$$$/ /$$$$$$$/| $$| $$  | $$  |  $$$$/
                    \_____/\___/ |__/|__/  \__/|__/| $$____/  \_______/ \_______/|__/ \_______/       \______/ |_______/ |__/|__/  |__/   \___/  
                                                   | $$                                                                                          
                                                   | $$                                                                                          
                                                   |__/                                                                                          

                                                      {2}Добро пожаловать на третью страницу по osint.
{2}
  
  Инструменты для расследований в Telegram.    {2}          
                                                                                                        
  Узнаем User ID {0}
    
  @userinfobot
  @CheckID_AIDbot
  @username_to_id_bot {2}

  История смены никнеймов {0}
  @SangMataInfo_bot {2}

  Поиск совпадений никнейма {0}
  @maigret_osint_bot {2}

  Дата создания аккаунта {0}
  @creationdatebot {2}

  Поисковики по Telegram {0}
    
  https://search.buzz.im/ 
  https://telemetr.me/
  http://telegcrack.com
  https://lyzem.com/
  https://tgstat.ru/
  https://cse.google.com/cse?&cx=006368593537057042503:efxu7xprihg#gsc.tab=0 {2}

  Выгружаем участников чата {0}
    
  @list_member_bot
  @quant_parserbot {2}

  Чаты пользователя {0}
   
  @telesint_bot
  @tgscanrobot {2}

  Узнаем телефон {0}
   
  @deanonym_bot
  @EyeGodsBot

  Узнаем IP-адрес пользователя {0}
   
  https://iplogger.ru/
  https://grabify.link/ {2}

{1}__________________________________________________________________________________________________________________________________{2}   
                                                                                                        
  Инструменты для деанонимизации по лицу.
    
  Поиск по фото в соцсетях {0}
    
  https://vk.watch/
  https://findclone.ru/
  https://pimeyes.com/en/
  https://search4faces.com/ {2}

  Боты {0}
   
  @AvinfoBot
  @Smart_SearchBot {2}

  Данные из поисковиков {0}
  https://yandex.ru/images/
  https://images.google.com/
  https://go.mail.ru/search_images
  https://tineye.com/ {2}

  Специализированное ПО {0}
    
  http://www.pictriev.com/
  http://betaface.com/demo.html
  https://azure.microsoft.com/ru-ru/services/cognitive-services/face/ {2}

  Ищем следы фотомонтажа {0}
    
  https://29a.ch/photo-forensics/#error-level-analysis {2}

  Определяем возраст {0}
    
  https://www.how-old.net/ {2}

  Определяем расу {0}
    
  https://en.vonvon.me/quiz/9447 {2}

  Составление фоторобота {0}
    
  http://foto.hotdrv.ru/fotorobot {2}

  Улучшение фото {0}
    
  https://www.myheritage.nl/photo-enhancer
  https://letsenhance.io/
  https://online-fotoshop.ru/fotoredaktor-online/ {2}
                                                                               
{1}__________________________________________________________________________________________________________________________________{2}  

  Оценка благонадежности граждан Беларуси.
   
  Международный розыск {0}
   
  https://www.interpol.int/How-we-work/Notices/View-Red-Notices {2}

  Национальный розыск {0}
  https://mvd.gov.by/ru/wanted {2}

  Банкротство {0}
  https://bankrot.gov.by/Debtors/DebtorsList {2}
   
  Исполнительные производства {0}
  https://minjust.gov.by/directions/enforcement/debtors/ {2}

  Налоговые задолженности {0}
  http://www.portal.nalog.gov.by/grp/#!fl {2}

  Участие в бизнесе {0}
  http://egr.gov.by/egrn/ {2}

  Участие в судопроизводстве {0}
  http://service.court.by/ru/public/schedule  {2}

  Поиск в соцсетях {0}
  https://go.mail.ru/search_social
  https://pipl.com 
           
{1}__________________________________________________________________________________________________________________________________{2}

  Мониторинг самолетов: {0}
  flightradar24.com
  radarbox.com
  planefinder.net {2}

  Мониторинг поездов:  {0}
  pass.rzd.ru {2}

  Мониторинг кораблей: {0}
  shipfinder.co
  vesselfinder.com
  marinetraffic.com {2}

  Мониторинг самолетов, поездов и маршрутного транспорта: {0}
  rasp.yandex.ru/map/ {2}

{1}__________________________________________________________________________________________________________________________________{2}

  Определяем владельца mail.ru
   
   
  Находим профиль в сервисе Мой Мир {0}
   
  http://my.mail.ru/mail/НИКНЕЙМ {2}

  Узнаем ID пользователя {0}
  http://appsmail.ru/platform/mail/НИКНЕЙМ {2}

  Ищем по никнейму в соцсетях {0} 
  https://go.mail.ru/search_social?q=НИКНЕЙМ {2}

  Получаем аватарку {0}
  http://filin.mail.ru/pic?width=180&height=180&email=example@mail.ru {2}

  Восстановление пароля {0}
  https://account.mail.ru/recovery 
  https://github.com/martinvigo/email2phonenumber  {2}

  Ищем аккаунты через соцсети {0}
   
  my.mail.ru/ok/ОДНОКЛАССНИКИ_ID
  my.mail.ru/vk/ВКОНТАКТЕ_ID 
  my.mail.ru/fb/ФЕЙСБУК_ID  {2}

  Ищем аккаунты через адрес эл.почты {0}
   
  my.mail.ru/gmail.com/LOGIN (часть email без @gmail.com)
  my.mail.ru/yandex.ru/LOGIN (часть email без @yandex.ru)
  my.mail.ru/mail/LOGIN (часть email без @mail.ru)
  my.mail.ru/SITE/LOGIN (поиск по любому никнейму)

{1}__________________________________________________________________________________________________________________________________{2}

  Деанонимизация пользователя Telegram через геолокацию. {0}
  
  https://telegra.ph/Telegram-publikuet-mestopolozhenie-polzovatelej-v-Internete-Perevod-01-05 

{1}__________________________________________________________________________________________________________________________________{2}

  Используем Солнце и тени для определения геолокации по фотографии {0}
  
  https://telegra.ph/Ispolzuem-Solnce-i-teni-dlya-opredeleniya-geolokacii-po-fotografii-12-22

{1}__________________________________________________________________________________________________________________________________{2}



{2}  OSINT в социальных сетях.
{0}
  Search by account in VK:
  searchlikes.ru • tutnaidut.com • 220vk.com  • @Smart_SearchBot • @VKUserInfo_bot • vk5.city4me.com • 
  vk.watch • vk-photo.xyz • vk-express.ru • archive.org • yasiv.com  • archive.is • @InfoVkUser_bot •
  @FindNameVk_bot • yzad.ru • vkdia.com • @EyeGodsBot

{2}  OSINT for account Twitter:
 {0}
  followerwonk.com • sleepingtime.org(r) • foller.me • socialbearing.com • keyhole.co  • analytics.mentionmapp.com  
  burrrd.com • keitharm.me • archive.org • @usersbox_bot • undelete.news • 

{2}  OSINT for account Facebook:
 {0}
  graph.tips • whopostedwhat.com • lookup-id.com • keyhole.co (r) • archive.org • @usersbox_bot • @GetPhone_bot •

{2}  OSINT For Instagram account:
 {0}
  gramfly.com • storiesig.com • codeofaninja.com • sometag.org • keyhole.co (r) • archive.org • @InstaBot • @usersbox_bot •
  undelete.news

{2}  OSINT For Reddit account:
 {0}
  snoopsnoo.com • redditinsight.com • redditinvestigator.com • archive.org • redditcommentsearch.com • 

{2}  OSINT For skype account:
 {0}
  mostwantedhf.info • cyber-hub.pw • webresolver.nl • @usersbox_bot 
 
 
{1}__________________________________________________________________________________________________________________________________{2}

  {1}Внимание, вы находитесь на странице ( 3 )

  {2}Дата последнего обновления:{0} вторник 27 января 2021г.

  {0}Проматай вверх сразу.

{1}__________________________________________________________________________________________________________________________________{2}


  {0}[ {1}99{0} ] {2}Выйти в главное меню...        {0}[ {1}0{0} ] {2}Предыдущая страница.
'''.format(GNSL, REDL, WHSL)
def main():
    print(page_1)
    print("")
    option = input(REDL + "  └──>" + ENDL +" Введите 99 для выхода : " +ENDL + " ")
    
    while(1):
        if option == '99':
            print("")
            print(("{1}  [ {0}+{1} ]{2} Спасибо за использование нашего Exploit.").format(REDL, GNSL, WHSL))
            os.system("cd ..;python3 osintsan.py")
            exit()
            option = input(ENDL + ""+GNSL+"["+REDL + " menu " + GNSL + "]"+ENDL + " :")
            
        elif option == '0':
            print(("{1}  [ {0}+{1} ]{2} Переход...{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("python3 Information_services2.py")
            exit()
            break
              
        else:
            os.system("python3 Information_services3.py")
try:
    main()

except KeyboardInterrupt:
    sys.exit(1)
except KeyboardInterrupt:
        print ("Ctrl+C pressed...")
