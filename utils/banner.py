from utils import COLORS

import random
import os

# dev by bafomet

BANNER1 = f""" {COLORS.REDL}
 {COLORS.REDL}{COLORS.GNSL}[{COLORS.WHSL} Official channel {COLORS.GNSL}tg {COLORS.REDL}@osint_san_framework {COLORS.REDL}{COLORS.GNSL}]            {COLORS.GNSL}[{COLORS.WHSL} GitHub {COLORS.REDL}https://github.com/Bafomet666 {COLORS.REDL}{COLORS.GNSL}]            {COLORS.GNSL}[ {COLORS.REDL}R{COLORS.WHSL} - c \xd1\x80\xd1\x83\xd1\x82\xd0\xbe\xd0\xbc.{COLORS.REDL} N{COLORS.WHSL} - \xd0\xb1\xd0\xb5\xd0\xb7 \xd1\x80\xd1\x83\xd1\x82\xd0\xb0 {COLORS.REDL}{COLORS.GNSL}]

                                  $$$$$$$\\                  $$\\        $$$$$$\\  $$\\                      $$\\     
                                  $$  __$$\\                 $$ |      $$  __$$\\ $$ |                     $$ |    
                                  $$ |  $$ | $$$$$$\\   $$$$$$$ |      $$ /  $$ |$$ | $$$$$$\\   $$$$$$\\ $$$$$$\\   
                                  $$$$$$$  |$$  __$$\\ $$  __$$ |      $$$$$$$$ |$$ |$$  __$$\\ $$  __$$\\ _$$  _|  
                                  $$  __$$< $$$$$$$$ |$$ /  $$ |      $$  __$$ |$$ |$$$$$$$$ |$$ |  \\__| $$ |    
                                  $$ |  $$ |$$   ____|$$ |  $$ |      $$ |  $$ |$$ |$$   ____|$$ |       $$ |$$\\ 
                                  $$ |  $$ |\\$$$$$$$\\ \\$$$$$$$ |      $$ |  $$ |$$ |\\$$$$$$$\\ $$ |       \\$$$$  |
                                  \\__|  \\__| \\_______| \\_______|      \\__|  \\__|\\__| \\_______|\\__|        \\____/ 

 {COLORS.WHSL}Framework :{COLORS.WHSL}{COLORS.GNSL} OSINT SAN.{COLORS.GNSL}
 {COLORS.WHSL}Update{COLORS.GNSL} RED Alert v-3.0
  """

BANNER2 = f"""{COLORS.GNSL}
 {COLORS.REDL}{COLORS.GNSL}[{COLORS.WHSL} Official channel {COLORS.GNSL}tg {COLORS.REDL}@osint_san_framework {COLORS.REDL}{COLORS.GNSL}]            {COLORS.GNSL}[{COLORS.WHSL} GitHub {COLORS.REDL}https://github.com/Bafomet666 {COLORS.REDL}{COLORS.GNSL}]            {COLORS.GNSL}[ {COLORS.REDL}R{COLORS.WHSL} - c \xd1\x80\xd1\x83\xd1\x82\xd0\xbe\xd0\xbc.{COLORS.REDL} N{COLORS.WHSL} - \xd0\xb1\xd0\xb5\xd0\xb7 \xd1\x80\xd1\x83\xd1\x82\xd0\xb0 {COLORS.REDL}{COLORS.GNSL}]

{COLORS.GNSL}                             _______   ________  _______          ______    ______   ______  __    __  ________  {COLORS.REDL}     __    __ 
{COLORS.GNSL}                            /       \\ /        |/       \\        /      \\  /      \\ /      |/  \\  /  |/        | {COLORS.REDL}    /  |  /  |
{COLORS.GNSL}                            $$$$$$$  |$$$$$$$$/ $$$$$$$  |      /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \\ $$ |$$$$$$$$/  {COLORS.REDL}    $$ |  $$ |
{COLORS.GNSL}                            $$ |__$$ |$$ |__    $$ |  $$ |      $$ |  $$ |$$ \\__$$/   $$ |  $$$  \\$$ |   $$ |    {COLORS.REDL}    $$  \\/$$/ 
{COLORS.GNSL}                            $$    $$< $$    |   $$ |  $$ |      $$ |  $$ |$$      \\   $$ |  $$$$  $$ |   $$ |    {COLORS.REDL}      $$ $$<  
{COLORS.GNSL}                            $$$$$$$  |$$$$$/    $$ |  $$ |      $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |    {COLORS.REDL}      $$$$  \\ 
{COLORS.GNSL}                            $$ |  $$ |$$ |_____ $$ |__$$ |      $$ \\__$$ |/  \\__$$ | _$$ |_ $$ |$$$$ |   $$ |    {COLORS.REDL}     $$ /$$  |
{COLORS.GNSL}                            $$ |  $$ |$$       |$$    $$/       $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |    {COLORS.REDL}    $$ |  $$ |
{COLORS.GNSL}                            $$/   $$/ $$$$$$$$/ $$$$$$$/         $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/     {COLORS.REDL}    $$/   $$/ 
                                                                                                                                                                                                                                                                                                                                                                                                                     
 {COLORS.WHSL}Framework :{COLORS.WHSL}{COLORS.GNSL} OSINT SAN.{COLORS.GNSL}
 {COLORS.WHSL}Update{COLORS.GNSL} RED Alert v-3.0
 """

BANNER3 = f"""
 {COLORS.REDL}{COLORS.GNSL}[{COLORS.WHSL} Official channel {COLORS.GNSL}tg {COLORS.REDL}@osint_san_framework {COLORS.REDL}{COLORS.GNSL}]            {COLORS.GNSL}[{COLORS.WHSL} GitHub {COLORS.REDL}https://github.com/Bafomet666 {COLORS.REDL}{COLORS.GNSL}]            {COLORS.GNSL}[ {COLORS.REDL}R{COLORS.WHSL} - c \xd1\x80\xd1\x83\xd1\x82\xd0\xbe\xd0\xbc.{COLORS.REDL} N{COLORS.WHSL} - \xd0\xb1\xd0\xb5\xd0\xb7 \xd1\x80\xd1\x83\xd1\x82\xd0\xb0 {COLORS.REDL}{COLORS.GNSL}]

{COLORS.GNSL}                 ______    ______   ______  __    __  ________         ______    ______   __    __    {COLORS.REDL}     ______    ______   ________  ________ 
{COLORS.GNSL}                /      \\  /      \\ /      |/  \\  /  |/        |       /      \\  /      \\ /  \\  /  |   {COLORS.REDL}    /      \\  /      \\ /        |/        |
{COLORS.GNSL}               /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \\ $$ |$$$$$$$$/       /$$$$$$  |/$$$$$$  |$$  \\ $$ |   {COLORS.REDL}   /$$$$$$  |/$$$$$$  |$$$$$$$$/ $$$$$$$$/ 
{COLORS.GNSL}               $$ |  $$ |$$ \\__$$/   $$ |  $$$  \\$$ |   $$ |         $$ \\__$$/ $$ |__$$ |$$$  \\$$ |   {COLORS.REDL}   $$____$$ |$$$  \\$$ |    /$$/      /$$/  
{COLORS.GNSL}               $$ |  $$ |$$      \\   $$ |  $$$$  $$ |   $$ |         $$      \\ $$    $$ |$$$$  $$ |   {COLORS.REDL}    /    $$/ $$$$  $$ |   /$$/      /$$/   
{COLORS.GNSL}               $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |          $$$$$$  |$$$$$$$$ |$$ $$ $$ |   {COLORS.REDL}   /$$$$$$/  $$ $$ $$ |  /$$/      /$$/    
{COLORS.GNSL}               $$ \\__$$ |/  \\__$$ | _$$ |_ $$ |$$$$ |   $$ |         /  \\__$$ |$$ |  $$ |$$ |$$$$ |   {COLORS.REDL}   $$ |_____ $$ \\$$$$ | /$$/      /$$/     
{COLORS.GNSL}               $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |         $$    $$/ $$ |  $$ |$$ | $$$ |   {COLORS.REDL}   $$       |$$   $$$/ /$$/      /$$/      
{COLORS.GNSL}                $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/           $$$$$$/  $$/   $$/ $$/   $$/    {COLORS.REDL}   $$$$$$$$/  $$$$$$/  $$/       $$/       
                                                                                                                                  
                                                                                    
 {COLORS.WHSL}Framework :{COLORS.WHSL}{COLORS.GNSL} OSINT SAN.{COLORS.GNSL}
 {COLORS.WHSL}Update{COLORS.GNSL} RED Alert v-3.0 
 """


def show_banner(*, clear=False):
    if clear:
        os.system("clear")
    banner = random.SystemRandom().choice([BANNER1, BANNER2, BANNER3])
    print(banner)


if __name__ == "__main__":
    show_banner()
