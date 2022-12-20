# from parsel import Selector
# import requests

# url = 'https://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
# response = requests.get(url=url)
# text = response.text
# selector = Selector(text=text)
# images = selector.css('img').xpath('@src').getall()
# image_url = []
# for image in images:
# 	imageurl = f"https://{image}"
# 	image_url.append(imageurl)
# print(image_url)

# import re

# text = "+8956785534"
# x = re.findall("^[].*[0-9]$",text)
# print(x)

# import json

# x = {"name":"abhi","age":"4","place":"knr"}
# # y = json.loads(x)
# y = json.dumps(x)
# # print(y['name'])
# print(y)

import csv

# with open('egs.csv','w') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerow(['Name','Place','Age'])
# 	writer.writerow(['Abhi','wnd','70'])

# with open('egs.csv','r') as csvfile:
# 	reader = csv.reader(csvfile)
# 	for row in reader:
# 		print(', '.join(row))

# with open('names.csv','w') as csvfile:
# 	fileds = ['name','place','age']
# 	writer = csv.DictWriter(csvfile,fileds)
# 	writer.writeheader()
# 	writer.writerow({
# 		'name':'Manu',
# 		'place':'kochi',
# 		'age':19
# 		})
# 	writer.writerow({
# 		'name':'suresh',
# 		'place':'vyppin',
# 		'age':20
# 		})

with open('names.csv','r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['name'],row['place'],row['age'])
