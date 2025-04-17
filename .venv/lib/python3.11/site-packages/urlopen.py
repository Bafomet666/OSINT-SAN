import urllib.request

gh_url = 'https://www.facebook.com'

auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(None, gh_url, 'patra.kailash@yahoo.com', 'jamesbond06')

opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
handler = urllib.request.urlopen(gh_url)

print(handler.getcode())
