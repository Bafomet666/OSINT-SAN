import requests
#Developer by Bafomet
def whois(wh):
    url = wh
    result = requests.get('http://api.hackertarget.com/whois/?q=' + url).text
    print('\n'+ result + '\n')
