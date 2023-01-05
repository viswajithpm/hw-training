import requests
from parsel import Selector
import csv


class Ebby():

	def __init__(self):

		self.headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
		}


	def parse_link(self,url):
		response = requests.get(url=url, headers=self.headers)
		print(response.status_code)
		if response.status_code != 200:
			raise Exception("Error")
		selector = Selector(text=response.text)
		name = selector.xpath('//h1//span[@class="account-title"]/text()').extract()
		print(name)

		for page in range(2,145):
			next_page = f"https://www.ebby.com/roster/agents/{page}"
			parse(next_page)


url = 'https://www.ebby.com/roster/agents/1'
ebby = Ebby()
ebby.parse_link(url)


# from lxml import etree

# root = etree.parse('/home/vpm/Downloads/sitemapbio.xml').getroot()
# print(root)
# url = root.find('url')
# loc = url.findall('loc')
# print(loc)
# # for grandchild in instrument:
#     code, source = grandchild.find('Code'), grandchild.find('Source')
#     print (code.text), (source.text)
