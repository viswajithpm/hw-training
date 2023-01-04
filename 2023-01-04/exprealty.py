import scrapy
from scrapy.crawler import CrawlerProcess

class Expreality(scrapy.Spider):
	name = 'expreality'
	url = ''
	headers = {
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

	def start_requests(self):
		yield scrapy.Requests(url=self.url, headers=self.headers, callback=self.parse)

	def parse(self,response):
		print(response.text)

process = CrawlerProcess()
process.crawl(Expreality)
process.start()