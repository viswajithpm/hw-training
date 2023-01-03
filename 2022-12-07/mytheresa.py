import requests
from parsel import Selector
import csv

class Mytheresa:

    def __init__(self):

        self.headers={
        'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        self.fields = [
        'breadcrumbs','image url','brand','product name','product id',
        'price','special_price','discount','sizes','description','other images'
        ]
        with open('mytheresa2.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fields)
            writer.writeheader()

    def parse(self, url):
        list1 = []
        result = requests.get(url=url, headers=self.headers)
        if result.status_code != 200:
            pass
        else:
            selector = Selector(text=result.text)

            amount = selector.xpath('//div[contains(@class,"product-shop")]')
            product = selector.xpath("//div[@class='main']")
            price = selector.xpath('//div[contains(@class,"price-info pa1-rmm-price")]')

            image = selector.xpath('//img[contains(@class,"gallery-image")]/@src').extract_first()
            image_url = f"https:{image}"

            sizes = []
            size_details = selector.xpath('//ul[contains(@class,"sizes")]//span/text()').extract()
            for size in size_details:
                size = size.split('/')
                for sze in size:
                    if sze.strip():
                        sizes.append(sze.strip())

            images = selector.xpath('//img[contains(@class,"gallery-image")]/@data-src').extract()
            other_images = []
            for image in images:
                imageurl = f"https:{image}"
                other_images.append(imageurl)

            description = (str(product.xpath('//p[contains(@class,"product-description")]/text()').extract_first())) + ' '.join(product.xpath("//li[@class='pa1-rmm']/text()").extract())
            listing_price = price.xpath('/div[contains(@class,"price-box")]/span/span/text()').extract_first()

            if listing_price is None:
                listing_price = price.xpath('//div/p[contains(@class,"old-price")]/span/text()').extract_first()

            dictionary = {

            "breadcrumbs":selector.xpath('//div[contains(@class,"breadcrumbs")]//span/text()').extract(),
            "image url":image_url,
            "brand":selector.xpath('//div[contains(@class,"product-designer")]/span/a/text()').extract_first(),
            "product name":selector.xpath('//div[contains(@class,"product-name")]/span/text()').extract_first(),
            "product id": amount.xpath('//span[contains(@class,"h1")]/text()').extract_first().replace('item no.\xa0',''),
            "price":listing_price,
            "special_price":price.xpath('//div/p[contains(@class,"special-price")]/span/text()').extract_first(),
            "discount":price.xpath('//span[contains(@class,"price-reduction-notice")]/text()').extract_first().replace("off","").strip(),
            "sizes":sizes,
            "description":description,
            "other images":other_images,

            }
        with open('mytheresa2.csv','a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fields)
            writer.writerow(dictionary)

    def parse_link(self, url):

        result = requests.get(url=url, headers=self.headers)
        if result.status_code != 200:
            pass
        else:
            selector1 = Selector(text=result.text)
            for link in selector1.xpath('//a[contains(@class,"product-image")]/@href').extract():
                mytheresa.parse(link)

        next_page=selector1.xpath('//li[contains(@class,"next")]/a/@href').extract_first()
        if next_page is not None:
            mytheresa.parse_link(next_page)

url = 'https://www.mytheresa.com/int_en/men/shoes.html'
mytheresa = Mytheresa()
mytheresa.parse_link(url)