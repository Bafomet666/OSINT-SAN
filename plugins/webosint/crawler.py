from settings import PROJECT_PATH

import os
import bs4
import requests

user_agent = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
}


def crawler(target, port):
	if port == 80:
		protocol = "http://"
	elif port == 443:
		protocol = "https://"
	else:
		print("Couldn't fetch data for the given PORT")
		return

	print('\n[+] Crawling Target...\n')
	target = protocol+target
	response = requests.get(target, headers=user_agent, verify=True, timeout=10)
	sc = response.status_code
	if sc != 200:
		print(f'[-] Error : {sc}')
		return

	domain = target.split('//')
	domain = domain[1]
	soup = bs4.BeautifulSoup(response.content, 'lxml')
	file = f'{domain}.dump'

	try:
		title = soup.title.string
	except AttributeError:
		title = 'None'

	external_sites_urls = get_urls_externals(domain)
	scrapped_urls_from_page = extract_urls_from_page(soup)
	internal_urls, external_urls = extract_all_href_links(soup, domain)

	total_urls = {
		**external_sites_urls,
		**scrapped_urls_from_page,
		"Internal Links": internal_urls,
		"External Links": external_urls,
	}
	number_of_all_urls = sum(map(len, total_urls.values()))
	print(f'\n[+] Total Links Extracted : {number_of_all_urls}\n')

	if number_of_all_urls:
		path_to_dump = os.path.join(PROJECT_PATH, "db", file)
		print(f'[+] Dumping Links in {path_to_dump}')
		with open(path_to_dump, 'w') as dumpfile:
			dumpfile.write(f'URL : {target}\n\n')
			dumpfile.write(f'Title: {title}\n')

			for name, urls in total_urls.items():
				dumpfile.write(
					f"\n{name} Links".rjust(19, ' ') + f": {len(urls)}"
				)

			dumpfile.write(f'\nTotal Links Found : {number_of_all_urls}\n')

			for name, urls in total_urls.items():
				if len(urls):
					dumpfile.write(f'\n{name} :\n\n')
					for url in urls:
						dumpfile.write(f"{url}\n")


def get_urls_externals(domain):
	all_urls = {}
	external_robots_txt_crawl = (
		"robots.txt",
		f'http://{domain}/robots.txt',
		collect_urls_from_robots_txt,
	)
	external_sitemap_crawl = (
		"sitemap.xml",
		f'http://{domain}/sitemap.xml',
		collect_urls_from_robots_txt,
	)

	for name, url, crawl_method in (external_robots_txt_crawl, external_sitemap_crawl):
		print(f'[+] Looking for {name}', end='')
		response = requests.get(
			url,
			headers=user_agent,
			verify=True,
			timeout=10,
		)
		status_code = response.status_code

		if status_code == 200:
			print('........[ Found ]')
			print('[+] Extracting...', end='')

			collected_urls = crawl_method(response)
			all_urls[name] = collected_urls

		elif status_code == 404:
			print('........[ Not Found ]')
		else:
			print(f'........[ {status_code} ]')

	return all_urls


def extract_urls_from_page(soup):
	all_urls = {}
	js_crawl = (
		"Javascript",
		extract_js_links,
	)
	css_crawl = (
		"CSS",
		extract_css_links,
	)
	image_crawl = (
		"Images",
		extract_image_links,
	)

	for name, crawl_method in (js_crawl, css_crawl, image_crawl):
		print(f'[+] Extracting {name}', end='')
		urls = crawl_method(soup)
		print(f'....[ {len(set(urls))} ]')
		all_urls[name] = urls

	return all_urls


def extract_all_href_links(soup, domain):
	external_links = []
	internal_links = []
	print("[+]Extracting Internal And External Links", end='')
	for link in soup.find_all('a'):
		url = link.get('href')
		if url:
			if domain in url:
				internal_links.append(url)
			elif 'http' in url:
				external_links.append(url)

	total_links = len(set(external_links) & set(internal_links))
	print(f'..............[ {total_links} ]')
	return internal_links, external_links


def collect_urls_from_robots_txt(response):
	robots_txt = response.text

	urls = []
	for entry in robots_txt.split('\n'):
		if 'Disallow' in entry or 'Allow' in entry:
			url = entry.split(':')

			try:
				url = url[1]
			except LookupError:
				continue
			else:
				url = url.strip()
				urls.append(url)

	return urls


def collect_urls_from_sitemap(response):
	sitemap = response.content

	urls = []
	sm_soup = bs4.BeautifulSoup(sitemap, 'xml')
	links = sm_soup.find_all('loc')
	for url in links:
		url = url.get_text()
		if url:
			urls.append(url)

	return urls


def extract_css_links(soup):
	links = []
	for link in soup.find_all('link'):
		url = link.get('href')
		if url and '.css' in url:
			links.append(url)
	return links


def extract_js_links(soup):
	links = []
	for script in soup.find_all('script'):
		url = script.get('src')
		if url and '.js' in url:
			links.append(url)
	return links


def extract_image_links(soup):
	links = []
	for img in soup.find_all('img'):
		url = img.get('src')
		if url is not None and len(url) > 1:
			links.append(url)

	return links


if __name__ == '__main__':
	crawler("google.com", 80)
