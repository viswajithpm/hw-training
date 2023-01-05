import requests
from parsel import Selector
import csv


class Alliebeth:

	def __init__(self):

		self.fields = ['first name', 'last name','title', 'description',
		'address', 'city', 'zipcode', 'state', 'agent phone', 'agent email', 'profile url\n']

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
		}
		with opn('alliebeth.csv','w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=fields)
			writer.writeheader()

	def parse(self,url):

		response = requests.get(url=url, headers=self.headers)
		if response.status_code != 200:
			raise Exception("Page Not Found")
		selector = Selector(text=response.text)

		details = {
			'name' = selector.xpath('//h1[@itemprop="name"]/text()').extract()
			'first_name' = name.split(' ')[0]
			'last_name' = name.split(' ')[1]
			'title' = selector.xpath('//h2[@itemprop="jobTitle"]/text()').extract_first()
			'description' = selector.xpath('//div[@itemprop="description"]/text').extract_first()
			'address' = selector.xpath('//div[@itemprop="streetAddress"]/text()').extract_first()
			'city' = selector.xpath('//span[@itemprop="addressLocality"]/text()').extract_first()
			'zip_code' = selector.xpath('//span[@itemprop="postalCode"]/text()').extract_first()
			'state' = selector.xpath('//span[@itemprop="addressRegion"]/text()').extract_first()
			'agent_phone' = selector.xpath('//a[contains(@class,"o-phone-number")]/text()').extract_first()
			'agent_email' = selector.xpath('//a[contains(@class,"listing-item__agent-email-address")]/text()').extract_first()
			'profile_url' = url
		}
	with open('alliebeth.csv','a') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fields)
		writer.writerow(details)


	def parse_link(self,url):
		response = requests.get(url=url, headers=self.headers)
		if response.status_code != 200:
			raise Exception("Page Not Found")
		selector = Selector(text=response.text)
		links = selector.xpath('//a[@class="url"]/@href').extract()
		for link in links:
			try:
				self.parse(link)
			except:
				continue
url = 'https://www.alliebeth.com/associates/int'
alliebeth = Alliebeth()
alliebeth.parse_link(url)
