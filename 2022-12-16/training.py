import requests
from parsel import Selector
import json
import csv

class Olx:
    def __init__(self):
        self.url = 'https://www.olx.in/api/relevance/v2/search?category=84&facet_limit=100&lang=en-IN&location=2001160&location_facet_limit=20&platform=web-desktop&size=40&user=1851487ee9fx3a22fd6d&page=1'
        self.headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            }

    def parse(self):
        result = requests.get(self.url,headers=self.headers)
        if result.status_code == 200:
            print(result)
            data = ''
            # with open('olx.json','w') as json_file:
            #     json_file.write(result.text)
            with open('olx.json','r') as json_file:
                for line in json_file.read():
                    data += line
            data = json.loads(data)
            for item in data['data']:
                # print(json.dumps(item, indent = 1))
                details = {
                    'title': item['title'],
                    'price': item['price']['value']['display']
                }
            next_page = data['metadata']['next_page_url']
                # print(json.dumps(details, indent=1))
                # with open('results.csv','a') as csv_file:
                #     writer = csv.DictWriter(csv_file, fieldnames=details.keys())
                #     writer.writerow(details)

olx = Olx()
olx.parse()
