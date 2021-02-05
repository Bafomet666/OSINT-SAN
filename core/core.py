#!/usr/bin/python
# -*- coding: utf-8 -*-
# Developer by Bafomet
from core.banner import show_banner
from utils import COLORS

import os

os.system("printf '\033]2;OSINT Attack mod\a'")
os.system("clear")
show_banner()

free_slot_text = f"{COLORS.WHSL}Свободный слот..."

PAGE = f"""                                                                                     
  {COLORS.GNSL}[ {COLORS.REDL}01{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}16{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}31{COLORS.GNSL} ] {free_slot_text}         {COLORS.REDL}Ожидайте в версиях 4.0 и выше...
  {COLORS.GNSL}[ {COLORS.REDL}02{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}17{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}32{COLORS.GNSL} ] {free_slot_text}         {COLORS.REDL}Буду пополнять по мере свободного времени.
  {COLORS.GNSL}[ {COLORS.REDL}03{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}18{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}33{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}04{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}19{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}34{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}05{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}20{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}35{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}06{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}21{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}36{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}07{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}22{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}37{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}08{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}23{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}38{COLORS.GNSL} ] {free_slot_text} 
  {COLORS.GNSL}[ {COLORS.REDL}09{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}24{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}39{COLORS.GNSL} ] {free_slot_text} 
  {COLORS.GNSL}[ {COLORS.REDL}10{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}25{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}40{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}11{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}26{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}41{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}12{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}27{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}42{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}13{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}28{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}43{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}14{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}29{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}44{COLORS.GNSL} ] {free_slot_text}
  {COLORS.GNSL}[ {COLORS.REDL}15{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}30{COLORS.GNSL} ] {free_slot_text}              {COLORS.GNSL}[ {COLORS.REDL}45{COLORS.GNSL} ] {free_slot_text}

  {COLORS.REDL}└──> {COLORS.GNSL} {COLORS.WHSL}Обратно в OSINT Menu.... {COLORS.GNSL}[{COLORS.REDL} 88 {COLORS.GNSL}]{COLORS.GNSL}        
  {COLORS.REDL}└──> {COLORS.GNSL} {COLORS.WHSL}Очистить...  {COLORS.GNSL}[{COLORS.REDL} 66 {COLORS.GNSL}]{COLORS.GNSL}

"""


def _main():
    print(PAGE)
    option = input(f"{COLORS.REDL}  └──>{COLORS.ENDL} Выберите опцию : {COLORS.ENDL} ")

    while True:
        if option == "88":
            print(f"\n{COLORS.GNSL}[ {COLORS.REDL}+{COLORS.GNSL} ]{COLORS.WHSL} Выполняем обратный переход.\n")
            show_banner(clear=True)
            return

        elif int(option) in range(1, 5):
            print(f"{COLORS.GNSL}[ {COLORS.REDL}+{COLORS.GNSL} ]{COLORS.WHSL} Переход...{COLORS.ENDL}")
            return

        elif option == "66":
            print(f"{COLORS.GNSL}[ {COLORS.REDL}+{COLORS.GNSL} ]{COLORS.WHSL} Переход...{COLORS.ENDL}")
            os.system("clear")
            _main()
            return

        else:
            _main()


def main():
    try:
        _main()
    except KeyboardInterrupt:
        print("Ctrl+C pressed...")


if __name__ == "__main__":
    main()
