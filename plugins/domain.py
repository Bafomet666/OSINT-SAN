#Developer by Bafomet
# -*- coding: utf-8 -*-
import os
import socket
from .webosint.CMSdetect import CMSdetect
from .webosint.nslookup import nsLookup
from .webosint.portscan import DefaultPort,Customrange
from .webosint.reverseip import ReverseIP
from .webosint.subdomain import SubDomain
from .webvuln.bruteforce import ssh
from .webvuln.clickjacking import ClickJacking
from .webvuln.cors import Cors
from .webvuln.hostheader import HostHeader
from .webosint.header import header
from .webosint.crawler import crawler
from .webosint.who.whoami import whoami
from .portscan import PortScan
from utils.banner import show_banner

R = '\033[31m'   # Red
G = '\033[1;34m' # Blue
C = '\033[1;32m' # Green
W = '\033[0m'    # white
O = '\033[45m'   # Purple

# Checking whether the target host is alive or dead
def CheckTarget(host, port):
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))

    if  result == 0:
        return True
    else:
        return False

# Main Method
def domain(host,port):

    if CheckTarget(host, port) == True:
        show_banner(clear=True)
        print("\n Выбирай опцию \n")
        Menu(host, port)
    else:
        print("The Host is Unreachable \n")


NmapFunctions = {
    1: DefaultPort,
    2: Customrange,
}


def nmaprec(host,port):
    try:
        Choice = 1
        while True:
            print("1. Scan Default Ports (22-443)")
            print("2. Enter Custom Range")
            print("3. Back to Main Menu")
            print()
            Choice = int(input(">> "))
            if (Choice >= 0) and (Choice < 3):
                NmapFunctions[Choice](host, port)
            elif Choice == 3:
                Menu(host,port)
            else:
                print("Please choose an Appropriate option")
    except AttributeError:
        PortScan(host)


BruteFunctions = {1: ssh}

def BruteForce(host, port):
    print("\nBrute Forcing SSH")
    BruteFunctions[1](host,port)


MainFunctions = {
 1: ReverseIP,
 2: SubDomain,
 3: nsLookup,
 4: CMSdetect,
 5: nmaprec,
 6: BruteForce,
 7: ClickJacking,
 8: Cors,
 9: HostHeader,
 10:header,
 11:crawler,
 }

def Menu(host,port): 
    Selection = 1
    while True:
        print('')
        print(G +  "[" + R + " 1 " + G + "]" +C + "  ReverseIP, SubDomain " + C + "\n")  
        print(G +  "[" + R + " 2 " + G + "]" +C + "  В разработке " + C + "\n")
        print(G +  "[" + R + " 3 " + G + "]" +C + "  NsLookup  " + C + "\n") 
        print(G +  "[" + R + " 4 " + G + "]" +C + "  CMS Detect " + C + "\n") 
        print(G +  "[" + R + " 5 " + G + "]" +C + "  Port Scan " + C + "\n")
        print(G +  "[" + R + " 6 " + G + "]" +C + "  Bruteforce " + C + "\n")
        print(G +  "[" + R + " 7 " + G + "]" +C + "  ClickJacking " + C + "\n")
        print(G +  "[" + R + " 8 " + G + "]" +C + "  CORS " + C + "\n")
        print(G +  "[" + R + " 9 " + G + "]" +C + "  Host Header Injection " + C + "\n")
        print(G +  "[" + R + " 10 " + G + "]" +C + " Header " + C + "\n") 
        print(G +  "[" + R + " 11 " + G + "]" +C + " Crawler " + C + "\n")  
        print(G +  "[" + R + " 99 " + G + "]" +C + " Exit")
        print('')
        Selection = int(input(C + "└──> Выбери опцию"+G+"[ "+R + "main_menu" + G + " ]"+G + " :"))
        if (Selection >= 0) and (Selection <=12):
            MainFunctions[Selection](host, port)
        elif Selection == 99:
            show_banner(clear=True)
            return
        else:
            print("Ошибка: выберите подходящий вариант")
        print()
