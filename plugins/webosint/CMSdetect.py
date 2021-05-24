from settings import cms_detect_api

import requests


def cms_detect(domain, port):
    if not cms_detect_api:
        print("[-]Нет ключа `cms_detect_api` (в settings.py)!")
        return
    payload = {'key': cms_detect_api, 'url': domain}
    cms_url = "https://whatcms.org/APIEndpoint/Detect"
    response = requests.get(cms_url, params=payload)
    cms_data = response.json()
    cms_info = cms_data['result']
    if cms_info['code'] == 200:
        print(f'Detected CMS     : {cms_info["name"]}')
        print(f'Detected Version : {cms_info["version"]}')
        print(f'Confidence       : {cms_info["confidence"]}')
    else:
        print(cms_info['msg'])
        print(f'Detected CMS : {cms_info["name"]}')
        print(f'Detected Version : {cms_info["version"]}')
