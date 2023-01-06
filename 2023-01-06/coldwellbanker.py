import requests
from parsel import Selector
import csv


class ColdwellBanker():

	def __init__(self):
		self.fields = ['country','first_name','middle_name','last_name','image_url','title', 'office_name', 'description', 'languages','address', 'city', 'zip_code', 'state', 'agent_phone','office_phone', 'social','website', 'agent_email', 'profile_url']
		self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
		}
		with open('coldwellbanker.csv','w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=self.fields)
			writer.writeheader()

	def parse(self,url):
		response = requests.get(url=url, headers=self.headers)
		print(response.status_code)
		selector = Selector(text=response.text)

		names = selector.xpath('//h1[@itemprop="name"]/text()').extract_first().strip().split(' ')
		first_name = names[0]
		if len(names) == 3:
			middle_name = names[1]
			last_name = names[2]
		else:
			middle_name = ""
			last_name = names[1]

		title = selector.xpath('//span[contains(@id,"agent-profile")]//span/text()').extract_first()
		languge = selector.xpath('//ul[contains(@class,"languages")]/li/text()')
		address = selector.xpath('https://docs.python.org/3/library/xml.etree.elementtree.html').extract()	
		

		

		
		

		# details = {
		# 'country': 'United states',
		# 'first_name': first_name,
		# 'middle_name': middle_name,
		# 'last_name': last_name,
		# 'image_url': selector.xpath('//img[@itemprop="image"]/@src').extract_first(),
		# 'title': "",
		# 'office_name': selector.xpath('//span[@class="mls-company-name"]/text()').extract_first().strip(),
		# 'description': selector.xpath('//span[@itemprop="description"]/text()').extract(),
		# 'languages': ,
		# 'address': ,
		# 'city': ,
		# 'zip_code': ,
		# 'state': ,
		# 'agent_phone': ,
		# 'office_phone': ,
		# 'social': ,
		# 'website': ,
		# 'agent_email': ,
		# 'profile_url': ,
		# }
		# with open('coldwellbanker.csv','a') as csvfile:
		# 	writer = csv.DictWriter(csvfile, fieldnames=self.fields)
		# 	writer.writerow(details)



	def parse_link(self,url):
		response = requests.get(url=url, headers=self.headers)
		print(response.status_code)
		if response.status_code != 200:
			raise Exception("Error")
		selector = Selector(text=response.text)
		name = selector.xpath('//h1//span[@class="account-title"]/text()').extract()
		print(name)

		# for page in range(2,145):
		# 	next_page = f"https://www.ebby.com/roster/agents/{page}"
		# 	parse(next_page)


url = 'https://www.coldwellbanker.com/coldwell-banker-select-realty-611c/lompoc-office-20543d'
cold = ColdwellBanker()
cold.parse(url)
