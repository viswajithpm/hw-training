import requests
from parsel import Selector
import csv

class Mytheresa:

    def __init__(self):

        self.headers={
        'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        with open('mytheresa1.csv', 'w') as csv_file:
            csv_file.write("breadcrumbs,image url,brand,product name,price,special_price,discount,sizes,description,other images\n")

    def parse(self, url):
        list1 = []
        result = requests.get(url=url, headers=self.headers)

        if result.status_code == 200:
            text = result.text
            selector = Selector(text=text)

            amount = selector.xpath('//div[contains(@class,"product-shop")]')
            product = selector.xpath("//div[@class='main']")
            price = amount.xpath('//div[contains(@class,"price-info pa1-rmm-price")]')

            image = selector.xpath('//img[contains(@class,"gallery-image")]/@src').get()
            image_url = f"https:{image}"

            sizes = []
            size_details = selector.xpath('//ul[contains(@class,"sizes")]//span/text()').getall()
            for size in size_details:
                size = size.split('/')
                for sze in size:
                    if sze.strip():
                        sizes.append(sze.strip())

            images = selector.xpath('//img[contains(@class,"gallery-image")]/@data-src').getall()
            other_images = []
            for image in images:
                imageurl = f"https:{image}"
                other_images.append(imageurl)

            description = (str(product.xpath('//p[contains(@class,"product-description")]/text()').get())) + ' '.join(product.xpath("//li[@class='pa1-rmm']/text()").getall())

            if price.xpath('//div/span/span/text()').get() is not None:

                dictionary = {

                "breadcrumbs":selector.xpath('//div[contains(@class,"breadcrumbs")]//span/text()').getall(),
                "image url":image_url,
                "brand":selector.xpath('//div[contains(@class,"product-designer")]/span/a/text()').get(),
                "product name":selector.xpath('//div[contains(@class,"product-name")]/span/text()').get(),
                "price":price.xpath('//div/span/span/text()').get(),
                "sizes":sizes,
                "description":description,
                "other images":other_images,

                }
            else:

                dictionary = {

                "breadcrumbs":selector.xpath('//div[contains(@class,"breadcrumbs")]//span/text()').getall(),
                "image url":image_url,
                "brand":selector.xpath('//div[contains(@class,"product-designer")]/span/a/text()').get(),
                "product name":selector.xpath('//div[contains(@class,"product-name")]/span/text()').get(),
                "price":price.xpath('//div/p[has-class("old-price")]/span/text()').get(),
                "special_price":price.xpath('//div/p[has-class("special-price")]/span/text()').get(),
                "discount":price.xpath('//span[has-class("price-reduction-notice")]/text()').get().replace("off","").strip(),
                "sizes":sizes,
                "description":description,
                "other images":other_images,

                }
        with open('mytheresa1.csv','a') as csvfile:
            fields = [
            'breadcrumbs','image url','brand','product name','price',
            'special_price','discount','sizes','description','other images'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writerow(dictionary)
            # writer.writeheader()

        # list1.append(dictionary)
        # dis_string=json.dumps(list1, indent=1)
        # f=open("mytheresa.json", "a")
        # f.write(dis_string)

    def parse_link(self, url):

        result = requests.get(url=url, headers=self.headers)
        if result.status_code == 200:
            text = result.text
            selector1 = Selector(text=text)
            for link in selector1.xpath('//a[contains(@class,"product-image")]/@href'):
                mytheresa.parse(link.get())

            next_page=selector1.xpath('//li[contains(@class,"next")]/a/@href').get()
            if next_page is not None:
                mytheresa.parse_link(next_page)

url = 'https://www.mytheresa.com/int_en/men/shoes.html'
mytheresa = Mytheresa()
mytheresa.parse_link(url)