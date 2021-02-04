import requests

def CMSdetect(domain, port):
    payload = {'key': 'замени меня на api', 'url': domain}
    cms_url = "https://whatcms.org/APIEndpoint/Detect"
    response = requests.get(cms_url, params=payload)
    cms_data = response.json()
    cms_info = cms_data['result']
    if cms_info['code'] == 200:
        print('Detected CMS     : %s' % cms_info['name'])
        print('Detected Version : %s' % cms_info['version'])
        print('Confidence       : %s' % cms_info['confidence'])
    else:
        print(cms_info['msg'])
        print('Detected CMS : %s' % cms_info['name'])
        print('Detected Version : %s' % cms_info['version'])
