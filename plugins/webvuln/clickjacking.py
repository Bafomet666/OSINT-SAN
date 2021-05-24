import requests


def click_jacking(host, port):
    if port == 80:
        protocol = 'http://'
    elif port == 443:
        protocol = 'https://'
    else:
        print("Couldn't fetch data for the given PORT")
        return

    url = f"{protocol}{host}"
    page = requests.get(url)

    if not "X-Frame-Options" in page.headers:
        print("Website is vulnerable to ClickJacking")
    else:
        print("Website is not Vulnerable to ClickJacking")
