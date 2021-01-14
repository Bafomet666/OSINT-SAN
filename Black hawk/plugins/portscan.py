from requests import get

#Developer by Bafomet
def PortScan(inp):
    result = get('http://api.hackertarget.com/nmap/?q=' + inp).text
    print('\n' + result + '\n')
