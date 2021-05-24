import requests


def reverse_ip(host, port):
    print('[+]Checking whether the Target is reachable ...\n')
    lookup = 'https://api.hackertarget.com/reverseiplookup/'
    try:
        result = requests.get(lookup, params={"q": host}).text
        print(result)
    except requests.exceptions.RequestException as e:
        print(f'Error: Invalid IP address {e}')
