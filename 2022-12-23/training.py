# from parsel import Selector

# text = '''<html>
# 			<body>
# 				<h1 class="h1" id="id1">Heading 1</h1>
# 				<h1 class="h1">Heading 2</h1>
# 				<h1 class="h1">Heading 3</h1>
# 				<label>This is a Label</label>
# 			</body>
# 		</html>'''
# selector = Selector(text=text)
# obj = selector.xpath('//h1[contains(@class,"h1")]/text()').getall()
# obj = selector.xpath('//h1[starts-with(@class,"h1")]/text()').get()
# obj = selector.xpath('//*[starts-with(name(),"l")]/text()').get()
# obj = selector.xpath('//h1[position()=1]/text()').get()
# obj = selector.xpath('//h1[last()]/text()').get()
# print(selector.xpath('count("h1")'))
# obj = selector.xpath('//*[@id="id1"]/text()').get()
# print(obj)