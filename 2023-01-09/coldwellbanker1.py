import requests
from parsel import Selector
import json
import re


class ColdwellBanker():

	def __init__(self):
		self.headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

		}

	def parse(self,url):
		response = requests.get(url=url, headers=self.headers)
		selector = Selector(text=response.text)
		office_link = selector.xpath("//a[contains(@class,'agent-link')]/@href").extract()
		for url in office_link:
			self.agent_details(f"https://www.coldwellbanker.com{url}")
	def agent_details(self, url):
		response = requests.get(url=url, headers=self.headers)
		selector = Selector(text=response.text)
		names = selector.xpath('//h1[@itemprop="name"]/text()').extract_first().strip().split(' ')
		first_name = names[0]
		if len(names) == 3:
			middle_name = names[1]
			last_name = names[2]
		else:
			middle_name = ""
			last_name = names[1]

		descriptn = selector.xpath('//div[@id="jsAgentProfile"]//text()').extract()
		des = ' '.join(descriptn)
		des = des.replace("\n","")
		description = re.sub(' +', ' ', des)

		image_url = selector.xpath('//img[@itemprop="photo"]/@src').extract_first()
		if image_url is None:
			image_url = selector.xpath('//img[@itemprop="image"]/@src').extract_first()

		title = selector.xpath('//span[contains(@id,"agent-profile")]//span/text()').extract_first()
		if title is None:
			title = ""

		address = selector.xpath('//div[@id="ft"]//div[@class="media__content"]/text()').extract()
		address1 = []
		for adrs in address:
			if adrs.isspace():
				continue
			else:
				address1.append(adrs.strip())
		ads = address1[1].split(' ')

		details = {
		'country': 'United states',
		'first_name': first_name,
		'middle_name': middle_name,
		'last_name': last_name,
		'image_url': image_url,
		'title': "",
		'office_name': selector.xpath('//span[@class="mls-company-name"]/text()').extract_first().strip(),
		'description': description.strip(),
		'languages': selector.xpath('//h2[contains(text(),"I Speak")]/following-sibling::ul/li/text()').extract(),
		'address': address1[0],
		'city': ads[0].replace(',',''),
		'zip_code': ads[2],
		'state': ads[1],
		'agent_phone': selector.xpath('//div[@itemprop="telephone"]/a[contains(@href,"tel")]/text()').extract(),
		'office_phone': selector.xpath('//div[@id="ft"]//a[contains(@href,"tel")]/text()').extract(),
		'social': "",
		'website': "",
		'agent_email': "",
		'profile_url': url,
		}
		dict_str = json.dumps(details)
		json_file = open('coldwellbanker1.json','a')
		json_file.write(dict_str+"\n")


	def parse_agent_link(self,url):
		response = requests.get(url=url, headers=self.headers)
		if response.status_code != 200:
			raise Exception("Page Not Found")
		selector = Selector(response.text)
		agent_url = selector.xpath("//url/loc/text()")[1].extract()
		self.parse(agent_url)

	def parse_office_link(self,url):
		response = requests.get(url=url, headers=self.headers)
		if response.status_code != 200:
			raise Exception("Error")
		selector = Selector(text=response.text)
		office_url = selector.xpath("//sitemap/loc/text()").extract()
		for url in office_url:
			self.parse_agent_link(url)

url = 'https://www.coldwellbanker.com/sitemap_brokers_index.xml'
cold = ColdwellBanker()
cold.parse_office_link(url)
