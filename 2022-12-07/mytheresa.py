import requests
from parsel import Selector
import json

class Mytheresa:
    def __init__(self):
        self.url = 'https://www.mytheresa.com/int_en/men/shoes.html'
        self.headers={'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    def parse(self):
        list1=[]
        result = requests.get(self.url,headers=self.headers)
        if result:
            text=result.text
            selector=Selector(text=text)
            amount = selector.xpath('//div[contains(@class,"product-shop")]')
            product = selector.xpath("//div[@class='main']")
            price = amount.xpath('//div[contains(@class,"price-info pa1-rmm-price")]')
            image = selector.css('img.gallery-image').xpath('@src').get()
            image_url = "https:%s"%image
            sizes = []
            size_details=selector.xpath("//div[@class='product-shop'] //ul[@class='sizes'] //span/text()").getall()
            for size in size_details:
                size = size.replace("/", " ").strip(" ").split("  ")
                for i in size:
                    sizes.append(i)
            images = selector.css('img.lazyload').xpath('@data-src').getall()
            other_images = []
            for image in images:
                imageurl = "https:%s"%image
                other_images.append(imageurl)
            description = (str(product.css('p.pa1-rmm.product-description::text').get())) + ' '.join(product.xpath("//li[@class='pa1-rmm']/text()").getall())
            if price.xpath('//div/span/span/text()').get() is not None:
                dictionary = {
                "breadcrumbs : ":selector.xpath('//div[contains(@class,"breadcrumbs")]//span/text()').getall(),
                "image url : ":image_url,
                "brand : ":selector.xpath('//div[contains(@class,"product-designer")]/span/a/text()').get(),
                "product name :":selector.xpath('//div[contains(@class,"product-name")]/span/text()').get(),
                "price : ":price.xpath('//div/span/span/text()').get(),
                "sizes : ":sizes,
                "description : ":description,
                "other images : ":other_images,
                }
            else:
                dictionary = {
                "breadcrumbs : ":selector.xpath('//div[contains(@class,"breadcrumbs")]//span/text()').getall(),
                "image url : ":image_url,
                "brand : ":selector.xpath('//div[contains(@class,"product-designer")]/span/a/text()').get(),
                "product name :":selector.xpath('//div[contains(@class,"product-name")]/span/text()').get(),
                "old_price : ":price.xpath('//div/p[has-class("old-price")]/span/text()').get(),
                "special_price : ":price.xpath('//div/p[has-class("special-price")]/span/text()').get(),
                "discount : ":price.xpath('//span[has-class("price-reduction-notice")]/text()').get().replace("off","").strip(),
                "sizes : ":sizes,
                "description : ":description,
                "other images : ":other_images,
                }
        list1.append(dictionary)
        dis_string=json.dumps(list1,indent=1)
        f=open("mytheresa.json","w")
        f.write(dis_string)
    def parse_link(self):
        result = requests.get(self.url,headers=self.headers)
        if result.status_code == 200:
            text=result.text
            selector1=Selector(text=text)
            for link in selector1.xpath('//a[contains(@class,"product-image")]/@href'):
                parse(link.get(),self.headers)
            next_page=selector1.xpath('//li[contains(@class,"next")]/a/@href').get()
            if next_page is not None:
                parse_link(next_page,self.headers)
        else:
            print("Error\n",result)
mytheresa = Mytheresa()
mytheresa.parse_link()