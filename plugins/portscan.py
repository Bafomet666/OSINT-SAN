import requests


#Developer by Bafomet
def portscan(inp):
    result = requests.get('http://api.hackertarget.com/nmap/', params={"q": inp}).text
    print(f'\n{result}\n')
