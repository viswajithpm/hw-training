import requests
from parsel import Selector
import json


url = 'https://www.mytheresa.com/int_en/men/shoes.html'
headers={'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


def parse(url,headers):
    result = requests.get(url,headers=headers)
    if result:
        text=result.text
        selector=Selector(text=text)

        amount = selector.xpath('//div[contains(@class,"product-shop")]')
        product = selector.xpath("//div[@class='main']")

        price = amount.xpath('//div[contains(@class,"price-info pa1-rmm-price")]')

        img = selector.css('img.gallery-image').xpath('@src').get()
        img_url = "https:%s"%img
        
        sizes = []
        size_details=selector.xpath("//div[@class='product-shop'] //ul[@class='sizes'] //span/text()").getall()
        for size in size_details:
            size = size.replace("/", " ").strip(" ").split("  ")
            for i in size:
                sizes.append(i)
        
        images = selector.css('img.lazyload').xpath('@data-src').getall()
        other_images = []
        for img in images:
            imgurl = "https:%s"%img
            other_images.append(imgurl)
        
        description = (str(product.css('p.pa1-rmm.product-description::text').get())) + ' '.join(product.xpath("//li[@class='pa1-rmm']/text()").getall())
        try:
            dictionary = {
            "breadcrumbs : ":selector.xpath('//div[contains(@class,"breadcrumbs")]//span/text()').getall(),
            "image url : ":img_url,
            "brand : ":selector.xpath('//div[contains(@class,"product-designer")]/span/a/text()').get(),
            "product name :":selector.xpath('//div[contains(@class,"product-name")]/span/text()').get(),
            "price : ":price.xpath('//div/span/span/text()').get(),
            "sizes : ":sizes,
            "description : ":description,
            "other images : ":other_images,
            }
        except:
            dictionary = {
            "breadcrumbs : ":selector.xpath('//div[contains(@class,"breadcrumbs")]//span/text()').getall(),
            "image url : ":img_url,
            "brand : ":selector.xpath('//div[contains(@class,"product-designer")]/span/a/text()').get(),
            "product name :":selector.xpath('//div[contains(@class,"product-name")]/span/text()').get(),
            "old_price : ":price.xpath('//div/p[has-class("old-price")]/span/text()').get(),
            "special_price : ":price.xpath('//div/p[has-class("special-price")]/span/text()').get(),
            "discount : ":price.xpath('//span[has-class("price-reduction-notice")]/text()').get().replace("off","").strip(),
            "sizes : ":sizes,
            "description : ":description,
            "other images : ":other_images,
            }
    lst.append(dictionary)
    with open("sample.json", "w") as outfile:
        json.dump(lst, outfile)
    return

def parse_link(url,headers):
    result = requests.get(url,headers=headers)
    print(result)
    if result:
        text=result.text
        selector1=Selector(text=text)
        for link in selector1.xpath('//a[contains(@class,"product-image")]/@href'):
            parse(link.get(),headers)
        next_page=selector1.xpath('//li[contains(@class,"next")]/a/@href').get()
        if next_page is not None:
            parse_link(next_page,headers)

lst=[]
parse_link(url=url,headers=headers)

