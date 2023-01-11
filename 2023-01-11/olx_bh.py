import requests
from parsel import Selector
import re

class Olx:
	def __init__(self):
		self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		}

	def parse(self,url):
		response = requests.get(url=url, headers=self.headers)
		print(response.status_code)
		selector = Selector(text=response.text)

		ID = re.findall("ID.+",url)

		cat_url = selector.xpath('//div[@aria-label="Breadcrumb"]//ul/li[5]/a/@href').extract_first()
		catagory_url = f"https://www.olx.com.bh{cat_url}"

		catogory = re.findall("Rent|Sales",cat_url)

		description = selector.xpath('//div[@aria-label="Details and description"]/div[2]//span/text()').extract()
		b = selector.xpath('//div[@aria-label="Overview"]//span[@aria-label="Location"]/text()').extract_first()


		print(b)
		

	# 	details = {
	# 	reference_number - 
	# 	'id': ' '.join(ID).replace(".html",""),
	# 	'url': url,
	# 	'broker_display_name': selector.xpath('//div[@aria-label="Seller description"]//a//span/text()').extract_first(),
	# 	'broker': 
	# 	'category': catagory[0],
	# 	category_url: catagory_url,
	# 	'title': selector.xpath('//div[@aria-label="Overview"]//h1').extract_first(),
	# 	'description': description[1],
	# 	location - Done
	# 	price - Done
	# 	currency - Done
	# 	price_per - Noted
	# 	bedrooms N
	# 	bathrooms N
	# 	furnished OK
	# 	rera_permit_number
	# 	dtcm_licence
	# 	scraped_ts
	# 	amenities - OK
	# 	details
	# 	agent_name
	# 	number_of_photos
	# 	user_id
	# 	phone_number
	# 	date
	# 	iteration_number
	# 	depth
	# 	sub_category_1
	# 	property_type
	# 	sub_category_2
	# 	published_at
	# 	listing_availability
	# 	}


	# def crawl_link(self,url):
	# 	response = requests.get(url=url, headers=self.headers)
	# 	print(response.status_code)
	# 	selector = Selector(text=response.text)
	# 	links = selector.xpath('//li[@aria-label="Listing"]//a/@href').extract()
	# 	links = [*set(links)]
	# 	for link in links:
	# 		link = f"https://www.olx.com.bh{link}"
	# 		self.parse(link)

		# next_page = selector.xpath('//li[last()]//a[contains(@href,"page")]/@href').extract_first()
		# if next_page is not None:
		# 	next_page = f"https://www.olx.com.bh{next_page}"
		# 	print(next_page)
		# 	self.crawl_link(next_page)


# urls = "https://www.olx.com.bh/en/properties/properties-for-sale/"
urls = 'https://www.olx.com.bh/en/ad/4bhk-flat-sale-ID104710964.html'
olx = Olx()
olx.parse(urls)