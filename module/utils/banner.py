from module.utils import COLORS

import random
import os
#-*- coding: utf-8 -*-
# dev by bafomet

BANNER1 = f"""
 {COLORS.REDL}{COLORS.GNSL}[{COLORS.WHSL} Official channel {COLORS.GNSL}tg {COLORS.REDL}@osint_san_framework {COLORS.REDL}{COLORS.GNSL}]    {COLORS.GNSL}[{COLORS.WHSL} GitHub {COLORS.REDL}https://github.com/Bafomet666 {COLORS.REDL}{COLORS.GNSL}]
{COLORS.GNSL}   ______    ______   ______  __    __  ________         ______    ______   __    __ 
{COLORS.GNSL}  /      \  /      \ /      |/  \  /  |/        |       /      \  /      \ /  \  /  | 
{COLORS.GNSL} /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \ $$ |$$$$$$$$/       /$$$$$$  |/$$$$$$  |$$  \ $$ |
{COLORS.GNSL} $$ |  $$ |$$ \__$$/   $$ |  $$$  \$$ |   $$ |         $$ \__$$/ $$ |__$$ |$$$  \$$ |   
{COLORS.GNSL} $$ |  $$ |$$      \   $$ |  $$$$  $$ |   $$ |         $$      \ $$    $$ |$$$$  $$ |    
{COLORS.GNSL} $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |          $$$$$$  |$$$$$$$$ |$$ $$ $$ |   
{COLORS.GNSL} $$ \__$$ |/  \__$$ | _$$ |_ $$ |$$$$ |   $$ |         /  \__$$ |$$ |  $$ |$$ |$$$$ |    
{COLORS.GNSL} $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |         $$    $$/ $$ |  $$ |$$ | $$$ |    
{COLORS.GNSL}  $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/           $$$$$$/  $$/   $$/ $$/   $$/  
{COLORS.REDL}  ,_._._._._._._._._|__________________________________________________________,
{COLORS.REDL}  |_|_|_|_|_|_|_|_|_|_________________________________________________________/
{COLORS.REDL}                    !   """
BANNER2 = f"""
 {COLORS.REDL}{COLORS.GNSL}[{COLORS.WHSL} Official channel {COLORS.GNSL}tg {COLORS.REDL}@osint_san_framework {COLORS.REDL}{COLORS.GNSL}]    {COLORS.GNSL}[{COLORS.WHSL} GitHub {COLORS.REDL}https://github.com/Bafomet666 {COLORS.REDL}{COLORS.GNSL}]
{COLORS.GNSL}   ______    ______   ______  __    __  ________         ______    ______   __    __ 
{COLORS.GNSL}  /      \  /      \ /      |/  \  /  |/        |       /      \  /      \ /  \  /  | 
{COLORS.GNSL} /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \ $$ |$$$$$$$$/       /$$$$$$  |/$$$$$$  |$$  \ $$ |
{COLORS.GNSL} $$ |  $$ |$$ \__$$/   $$ |  $$$  \$$ |   $$ |         $$ \__$$/ $$ |__$$ |$$$  \$$ |   
{COLORS.GNSL} $$ |  $$ |$$      \   $$ |  $$$$  $$ |   $$ |         $$      \ $$    $$ |$$$$  $$ |    
{COLORS.GNSL} $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |          $$$$$$  |$$$$$$$$ |$$ $$ $$ |   
{COLORS.GNSL} $$ \__$$ |/  \__$$ | _$$ |_ $$ |$$$$ |   $$ |         /  \__$$ |$$ |  $$ |$$ |$$$$ |    
{COLORS.GNSL} $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |         $$    $$/ $$ |  $$ |$$ | $$$ |    
{COLORS.GNSL}  $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/           $$$$$$/  $$/   $$/ $$/   $$/  
{COLORS.REDL}  ,_._._._._._._._._|__________________________________________________________,
{COLORS.REDL}  |_|_|_|_|_|_|_|_|_|_________________________________________________________/
{COLORS.REDL}                    !   """
BANNER3 = f"""
 {COLORS.REDL}{COLORS.GNSL}[{COLORS.WHSL} Official channel {COLORS.GNSL}tg {COLORS.REDL}@osint_san_framework {COLORS.REDL}{COLORS.GNSL}]    {COLORS.GNSL}[{COLORS.WHSL} GitHub {COLORS.REDL}https://github.com/Bafomet666 {COLORS.REDL}{COLORS.GNSL}]
{COLORS.GNSL}   ______    ______   ______  __    __  ________         ______    ______   __    __ 
{COLORS.GNSL}  /      \  /      \ /      |/  \  /  |/        |       /      \  /      \ /  \  /  | 
{COLORS.GNSL} /$$$$$$  |/$$$$$$  |$$$$$$/ $$  \ $$ |$$$$$$$$/       /$$$$$$  |/$$$$$$  |$$  \ $$ |
{COLORS.GNSL} $$ |  $$ |$$ \__$$/   $$ |  $$$  \$$ |   $$ |         $$ \__$$/ $$ |__$$ |$$$  \$$ |   
{COLORS.GNSL} $$ |  $$ |$$      \   $$ |  $$$$  $$ |   $$ |         $$      \ $$    $$ |$$$$  $$ |    
{COLORS.GNSL} $$ |  $$ | $$$$$$  |  $$ |  $$ $$ $$ |   $$ |          $$$$$$  |$$$$$$$$ |$$ $$ $$ |   
{COLORS.GNSL} $$ \__$$ |/  \__$$ | _$$ |_ $$ |$$$$ |   $$ |         /  \__$$ |$$ |  $$ |$$ |$$$$ |    
{COLORS.GNSL} $$    $$/ $$    $$/ / $$   |$$ | $$$ |   $$ |         $$    $$/ $$ |  $$ |$$ | $$$ |    
{COLORS.GNSL}  $$$$$$/   $$$$$$/  $$$$$$/ $$/   $$/    $$/           $$$$$$/  $$/   $$/ $$/   $$/  
{COLORS.REDL}  ,_._._._._._._._._|__________________________________________________________,
{COLORS.REDL}  |_|_|_|_|_|_|_|_|_|_________________________________________________________/
{COLORS.REDL}                    !   """

def show_banner(*, clear=False):
    if clear:
        os.system("clear")
    banner = random.SystemRandom().choice([BANNER1, BANNER2, BANNER3])
    print(banner)


if __name__ == "__main__":
    show_banner()
