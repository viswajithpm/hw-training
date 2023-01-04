import requests
from parsel import Selector


class Allman:

	def __init__(self):

		self.headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'cross-site',
		'sec-fetch-user': '?1',
		'referer': 'https://exprealty.com/agents/'
		}

	def parse_link(self,url):
		response = requests.get(url=url, headers=self.headers)
		print(response.status_code)
		selector = Selector(text=response.text)
		# print(selector)
		names = selector.xpath('/html/body/div[4]/div/div/section[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/a[1]/div/div[1]').extract_first()
		print(names)

url = 'https://exprealty.com/agents'
allman = Allman()
allman.parse_link(url)
