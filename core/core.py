#!/usr/bin/python
# -*- coding: utf-8 -*-
# Developer by Bafomet
from core.banner import show_banner

import os

# set color
WHSL = "\033[1;32m"
ENDL = "\033[0m"
REDL = "\033[0;31m"
GNSL = "\033[1;34m"

os.system("printf '\033]2;OSINT Attack mod\a'")
os.system("clear")
show_banner()

free_slot_text = f"{WHSL}Свободный слот..."

PAGE = f"""                                                                                     
  {GNSL}[ {REDL}01{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}16{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}31{GNSL} ] {free_slot_text}         {REDL}Ожидайте в версиях 4.0 и выше...
  {GNSL}[ {REDL}02{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}17{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}32{GNSL} ] {free_slot_text}         {REDL}Буду пополнять по мере свободного времени.
  {GNSL}[ {REDL}03{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}18{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}33{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}04{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}19{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}34{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}05{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}20{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}35{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}06{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}21{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}36{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}07{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}22{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}37{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}08{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}23{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}38{GNSL} ] {free_slot_text} 
  {GNSL}[ {REDL}09{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}24{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}39{GNSL} ] {free_slot_text} 
  {GNSL}[ {REDL}10{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}25{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}40{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}11{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}26{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}41{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}12{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}27{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}42{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}13{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}28{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}43{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}14{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}29{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}44{GNSL} ] {free_slot_text}
  {GNSL}[ {REDL}15{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}30{GNSL} ] {free_slot_text}              {GNSL}[ {REDL}45{GNSL} ] {free_slot_text}

  {REDL}└──> {GNSL} {WHSL}Обратно в OSINT Menu.... {GNSL}[{REDL} 88 {GNSL}]{GNSL}        
  {REDL}└──> {GNSL} {WHSL}Очистить...  {GNSL}[{REDL} 66 {GNSL}]{GNSL}

"""


def _main():
    print(PAGE)
    option = input(f"{REDL}  └──>{ENDL} Выберите опцию : {ENDL} ")

    while True:
        if option == "88":
            print(f"\n{GNSL}[ {REDL}+{GNSL} ]{WHSL} Выполняем обратный переход.\n")
            show_banner(clear=True)
            return

        elif int(option) in range(1, 5):
            print(f"{GNSL}[ {REDL}+{GNSL} ]{WHSL} Переход...{ENDL}")
            return

        elif option == "66":
            print(f"{GNSL}[ {REDL}+{GNSL} ]{WHSL} Переход...{ENDL}")
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
