import random
import os

# dev by bafomet
# Set color
WHSL = "\033[1;32m"
ENDL = "\033[0m"
REDL = "\033[0;31m"
GNSL = "\033[1;34m"

BANNER1 = f""" {REDL}
 {REDL}{GNSL}[{WHSL} Official channel {GNSL}tg {REDL}@osint_san_framework {REDL}{GNSL}]            {GNSL}[{WHSL} GitHub {REDL}https://github.com/Bafomet666 {REDL}{GNSL}]            {GNSL}[ {REDL}R{WHSL} - c \xd1\x80\xd1\x83\xd1\x82\xd0\xbe\xd0\xbc.{REDL} N{WHSL} - \xd0\xb1\xd0\xb5\xd0\xb7 \xd1\x80\xd1\x83\xd1\x82\xd0\xb0 {REDL}{GNSL}]

                                  $$$$$$$\\                  $$\\        $$$$$$\\  $$\\                      $$\\     
                                  $$  __$$\\                 $$ |      $$  __$$\\ $$ |                     $$ |    
                                  $$ |  $$ | $$$$$$\\   $$$$$$$ |      $$ /  $$ |$$ | $$$$$$\\   $$$$$$\\ $$$$$$\\   
                                  $$$$$$$  |$$  __$$\\ $$  __$$ |      $$$$$$$$ |$$ |$$  __$$\\ $$  __$$\\ _$$  _|  
                                  $$  __$$< $$$$$$$$ |$$ /  $$ |      $$  __$$ |$$ |$$$$$$$$ |$$ |  \\__| $$ |    
                                  $$ |  $$ |$$   ____|$$ |  $$ |      $$ |  $$ |$$ |$$   ____|$$ |       $$ |$$\\ 
                                  $$ |  $$ |\\$$$$$$$\\ \\$$$$$$$ |      $$ |  $$ |$$ |\\$$$$$$$\\ $$ |       \\$$$$  |
                                  \\__|  \\__| \\_______| \\_______|      \\__|  \\__|\\__| \\_______|\\__|        \\____/ 

 {WHSL}Framework :{WHSL}{GNSL} OSINT SAN.{GNSL}
 {WHSL}Update{GNSL} RED Alert v-3.0
  """

BANNER2 = f"""{GNSL}
 {REDL}{GNSL}[{WHSL} Official channel {GNSL}tg {REDL}@osint_san_framework {REDL}{GNSL}]            {GNSL}[{WHSL} GitHub {REDL}https://github.com/Bafomet666 {REDL}{GNSL}]            {GNSL}[ {REDL}R{WHSL} - c \xd1\x80\xd1\x83\xd1\x82\xd0\xbe\xd0\xbc.{REDL} N{WHSL} - \xd0\xb1\xd0\xb5\xd0\xb7 \xd1\x80\xd1\x83\xd1\x82\xd0\xb0 {REDL}{GNSL}]

{GNSL}                             _______   ________  _______          ______    ______   ______  __    __  ________  {REDL}     __    __ 
{GNSL}                            /       \\ /        |/       \\        /      \\  /      \\ /      |/  \\  /  |/        | {REDL}    /  |  /  |
{GNSL}                            $$$$$$$  |$$$$$$$$/ $$$$$$$  |      /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \\ $$ |$$$$$$$$/  {REDL}    $$ |  $$ |
{GNSL}                            $$ |__$$ |$$ |__    $$ |  $$ |      $$ |  $$ |$$ \\__$$/   $$ |  $$$  \\$$ |   $$ |    {REDL}    $$  \\/$$/ 
{GNSL}                            $$    $$< $$    |   $$ |  $$ |      $$ |  $$ |$$      \\   $$ |  $$$$  $$ |   $$ |    {REDL}      $$ $$<  
{GNSL}                            $$$$$$$  |$$$$$/    $$ |  $$ |      $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |    {REDL}      $$$$  \\ 
{GNSL}                            $$ |  $$ |$$ |_____ $$ |__$$ |      $$ \\__$$ |/  \\__$$ | _$$ |_ $$ |$$$$ |   $$ |    {REDL}     $$ /$$  |
{GNSL}                            $$ |  $$ |$$       |$$    $$/       $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |    {REDL}    $$ |  $$ |
{GNSL}                            $$/   $$/ $$$$$$$$/ $$$$$$$/         $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/     {REDL}    $$/   $$/ 
                                                                                                                                                                                                                                                                                                                                                                                                                     
 {WHSL}Framework :{WHSL}{GNSL} OSINT SAN.{GNSL}
 {WHSL}Update{GNSL} RED Alert v-3.0
 """

BANNER3 = f"""
 {REDL}{GNSL}[{WHSL} Official channel {GNSL}tg {REDL}@osint_san_framework {REDL}{GNSL}]            {GNSL}[{WHSL} GitHub {REDL}https://github.com/Bafomet666 {REDL}{GNSL}]            {GNSL}[ {REDL}R{WHSL} - c \xd1\x80\xd1\x83\xd1\x82\xd0\xbe\xd0\xbc.{REDL} N{WHSL} - \xd0\xb1\xd0\xb5\xd0\xb7 \xd1\x80\xd1\x83\xd1\x82\xd0\xb0 {REDL}{GNSL}]

{GNSL}                 ______    ______   ______  __    __  ________         ______    ______   __    __    {REDL}     ______    ______   ________  ________ 
{GNSL}                /      \\  /      \\ /      |/  \\  /  |/        |       /      \\  /      \\ /  \\  /  |   {REDL}    /      \\  /      \\ /        |/        |
{GNSL}               /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \\ $$ |$$$$$$$$/       /$$$$$$  |/$$$$$$  |$$  \\ $$ |   {REDL}   /$$$$$$  |/$$$$$$  |$$$$$$$$/ $$$$$$$$/ 
{GNSL}               $$ |  $$ |$$ \\__$$/   $$ |  $$$  \\$$ |   $$ |         $$ \\__$$/ $$ |__$$ |$$$  \\$$ |   {REDL}   $$____$$ |$$$  \\$$ |    /$$/      /$$/  
{GNSL}               $$ |  $$ |$$      \\   $$ |  $$$$  $$ |   $$ |         $$      \\ $$    $$ |$$$$  $$ |   {REDL}    /    $$/ $$$$  $$ |   /$$/      /$$/   
{GNSL}               $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |          $$$$$$  |$$$$$$$$ |$$ $$ $$ |   {REDL}   /$$$$$$/  $$ $$ $$ |  /$$/      /$$/    
{GNSL}               $$ \\__$$ |/  \\__$$ | _$$ |_ $$ |$$$$ |   $$ |         /  \\__$$ |$$ |  $$ |$$ |$$$$ |   {REDL}   $$ |_____ $$ \\$$$$ | /$$/      /$$/     
{GNSL}               $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |         $$    $$/ $$ |  $$ |$$ | $$$ |   {REDL}   $$       |$$   $$$/ /$$/      /$$/      
{GNSL}                $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/           $$$$$$/  $$/   $$/ $$/   $$/    {REDL}   $$$$$$$$/  $$$$$$/  $$/       $$/       
                                                                                                                                  
                                                                                    
 {WHSL}Framework :{WHSL}{GNSL} OSINT SAN.{GNSL}
 {WHSL}Update{GNSL} RED Alert v-3.0 
 """


def show_banner(*, clear=False):
    if clear:
        os.system("clear")
    banner = random.SystemRandom().choice([BANNER1, BANNER2, BANNER3])
    print(banner)


if __name__ == "__main__":
    show_banner()
