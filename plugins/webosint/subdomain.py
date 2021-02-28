import requests

from settings import virustotal_api


def subdomain(host, port):
    print('[+]Fetching Subdomains of Target...\n')
    if not virustotal_api:
        print("[-]Не найден ключ `virustotal_api` (в settings.py)!")
        return
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'

    params = {
        'apikey': virustotal_api,
        'domain': host,
    }
    response = requests.get(url, params=params)

    subdomains = response.json()
    for x in subdomains['subdomains']:
        print(x)
