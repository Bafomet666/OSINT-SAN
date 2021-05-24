import requests

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white


def ns_lookup(host, port):
    print('[+]Fetching Details...\n')
    result = requests.get(
        'http://api.hackertarget.com/dnslookup/',
        params={"q": host}
    ).text
    print(result)
