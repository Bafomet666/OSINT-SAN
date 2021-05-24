#Developer by Bafomet
# -*- coding: utf-8 -*-
import os
import socket
from .webosint.CMSdetect import cms_detect
from .webosint.nslookup import ns_lookup
from .webosint.portscan import default_ports_scan, custom_range_ports_scan
from .webosint.reverseip import reverse_ip
from .webosint.subdomain import subdomain
from .webvuln.bruteforce import ssh
from .webvuln.clickjacking import click_jacking
from .webvuln.cors import cors
from .webvuln.hostheader import host_header
from .webosint.header import header
from .webosint.crawler import crawler
from .webosint.who.whoami import whoami
from .portscan import portscan
from module.utils.banner import show_banner

R = '\033[31m'    # Red
G = '\033[1;34m'  # Blue
C = '\033[1;32m'  # Green
W = '\033[0m'     # white
O = '\033[45m'    # Purple


# Checking whether the target host is alive or dead
def check_target(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))

    return result == 0


# Main Method
def domain(host, port):
    if check_target(host, port):
        show_banner(clear=True)
        print("\n Выберите опцию")
        menu(host, port)
    else:
        print("The Host is Unreachable \n")


nmap_functions = {
    1: default_ports_scan,
    2: custom_range_ports_scan,
}


def nmaprec(host, port):
    try:
        while True:
            print("1. Scan Default Ports (22-443)")
            print("2. Enter Custom Range")
            print("3. Back to Main Menu")
            print()
            choice = int(input(">> "))
            if 0 <= choice < 3:
                nmap_functions[choice](host, port)
            elif choice == 3:
                menu(host, port)
            else:
                print("Please choose an Appropriate option")
    except AttributeError:
        portscan(host)


def bruteforce(host, port):
    print("\nBrute Forcing SSH")
    ssh(host, port)


option_to_function = {
 1: reverse_ip,
 2: subdomain,
 3: ns_lookup,
 4: cms_detect,
 5: nmaprec,
 6: bruteforce,
 7: click_jacking,
 8: cors,
 9: host_header,
 10: header,
 11: crawler,
 }


def menu(host, port):
    while True:
        print()
        print(f"{G} [{R} 1 {G}]{C}  ReverseIP, SubDomain {C}")
        print(f"{G} [{R} 2 {G}]{C}  В разработке {C}")
        print(f"{G} [{R} 3 {G}]{C}  NsLookup  {C}")
        print(f"{G} [{R} 4 {G}]{C}  CMS Detect {C}")
        print(f"{G} [{R} 5 {G}]{C}  Port Scan {C}")
        print(f"{G} [{R} 6 {G}]{C}  Bruteforce {C}")
        print(f"{G} [{R} 7 {G}]{C}  ClickJacking {C}")
        print(f"{G} [{R} 8 {G}]{C}  CORS {C}")
        print(f"{G} [{R} 9 {G}]{C}  Host Header Injection {C}")
        print(f"{G} [{R} 10 {G}]{C} Header {C}")
        print(f"{G} [{R} 11 {G}]{C} Crawler {C}")
        print(f"{G} [{R} 99 {G}]{C} Exit")
        print()
        try:
            selection = int(input(f"{C} └──> Выберите опцию {G}[ {R}main_menu{G} ]{G} :"))
        except KeyboardInterrupt:
            return
        if 0 <= selection <= 12:
            os.system("clear")
            run_command = option_to_function[selection]
            run_command(host, port)
        elif selection == 99:
            return
            show_banner(clear=True)
        else:
            print("Ошибка: выберите подходящий вариант")
        print()
