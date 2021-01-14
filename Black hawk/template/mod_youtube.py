#!/usr/bin/env python3

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

redirect = input(G + '[+]' + C + ' Запустить ? yes / no : ' + W)
with open('template/Youtube/js/location_temp.js', 'r') as js:
	reader = js.read()
	update = reader.replace('REDIRECT_URL', redirect)

with open('template/Youtube/js/location.js', 'w') as js_update:
	js_update.write(update)
