import requests


def cors(host, port):
    if port == 80:
        protocol = 'http://'
    elif port == 443:
        protocol = 'https://'
    else:
        print("Couldn't fetch data for the given PORT")
        return

    print("1. CORS check in Default Host")
    print("2. CORS check in Host's Custom Endpoint")

    print()
    choice = int(input('CORS >>'))
    print()

    cookies = input("Paste the Cookies (If None,then hit enter) : ")
    if cookies == '':
        cookies_header = {}
    else:
        cookies_header = {"Cookie": cookies}

    evil_domain = "evil.com"
    host_domain = f"{host}.evil.com"
    host_domain_with_payload = f"{host}%60cdl.evil.com"
    headers = {
        evil_domain: {"Origin": f"http://{evil_domain}", **cookies_header},
        host_domain: {"Origin": f"{protocol}{host_domain}", **cookies_header},
        host_domain_with_payload: {
            "Origin": f"{protocol}{host_domain_with_payload}",
            **cookies_header,
        },
    }

    if choice == 2:
        host = input("Enter the Custom Endpoint : ")

    url = protocol + host
    check_vulnerable_to_cors(url, headers)


def check_vulnerable_to_cors(url, headers):
    for domain, header in headers.items():
        print(f"Testing with Payload {header}")
        response = requests.get(url, headers=header)
        if domain in response.headers:
            print("Vulnerable to Cross Origin Resource Sharing")
        else:
            print("Not Vulnerable to Cross Origin Resource Sharing")
        print()


if __name__ == '__main__':
    cors("google.com", 80)
