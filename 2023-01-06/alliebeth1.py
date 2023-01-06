import requests
from parsel import Selector
import csv


class Alliebeth:

	def __init__(self):
		self.fields = ['first_name','last_name','image_url','title', 'description', 'address', 'city', 'zip_code', 'state', 'agent_phone', 'agent_email', 'profile_url']
		self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		}

		with open('alliebeth.csv', 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=self.fields)
			writer.writeheader()

	def parse(self,url):

		response = requests.get(url=url, headers=self.headers)
		if response.status_code != 200:
			raise Exception("Page Not Found")
		else:
			selector = Selector(text=response.text)
			image = selector.xpath('//div[@id="agentphoto"]//img/@src').extract_first().replace('&imagecache=true','')
			image_url = f"https:{image}"
			description = selector.xpath('//div[@itemprop="description"]//*/text()').extract()
			if not description:
				description = selector.xpath('//div[@itemprop="description"]/text()').extract()
			description1 = []
			for des in description:
				if des == ' ':
					continue
				else:
					description1.append(des)

			for name in selector.xpath('//h1[@itemprop="name"]/text()').extract():
				first_name = name.split(' ')[0]
				last_name = name.split(' ')[1]

			details = {
		
			"first_name": first_name,
			"last_name": last_name,
			"image_url": image_url,
			"title": selector.xpath('//h2[@itemprop="jobTitle"]/text()').extract_first().strip(),
			"description": description1,
			"address": selector.xpath('//div[@itemprop="streetAddress"]/text()').extract_first(),
			"city": selector.xpath('//span[@itemprop="addressLocality"]/text()').extract_first(),
			"zip_code": selector.xpath('//span[@itemprop="postalCode"]/text()').extract_first(),
			"state": selector.xpath('//span[@itemprop="addressRegion"]/text()').extract_first(),
			"agent_phone": selector.xpath('//a[contains(@class,"o-phone-number")]/text()').extract_first(),
			"agent_email": selector.xpath('//a[contains(@class,"listing-item__agent-email-address")]/text()').extract_first(),
			"profile_url": url,
			}

			with open('alliebeth.csv','a') as csvfile:
				writer = csv.DictWriter(csvfile,fieldnames=self.fields)
				writer.writerow(details)


	def parse_link(self,url):
		response = requests.get(url=url, headers=self.headers)
		if response.status_code != 200:
			raise Exception("Page Not Found")
		selector = Selector(text=response.text)
		links = selector.xpath('//a[@class="url"]/@href').extract()
		for link in links:
			try:
				alliebeth.parse(link)
			except:
				continue
		next_page = selector.xpath('//a[@aria-label="Next Page"]/@href').extract_first()
		if next_page is not None:
			next_page = f"https://www.alliebeth.com{next_page}"
			alliebeth.parse_link(next_page)

url = 'https://www.alliebeth.com/associates/int'
alliebeth = Alliebeth()
alliebeth.parse_link(url)
