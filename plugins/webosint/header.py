import requests
requests.packages.urllib3.disable_warnings()


def header(target, port):
	if port == 80:
		protocol = "http://"
	elif port == 443:
		protocol = "https://"
	else:
		print("Couldn't fetch data for the given PORT")
		return
	print('\n[+] Headers :\n')

	response = requests.get(protocol+target, verify=True, timeout=10)
	for k, v in response.headers.items():
		print(f'[+] {k} : {v}')
