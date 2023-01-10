import requests
import json

class Exprealty:
	def __init__(self):
		self.headers = {
		"content-type": "application/json",
        "origin": "https://exprealty.com",
        "referer": "https://exprealty.com/",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Linux",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
		}
		self.payload={"operationName":"SearchQuery",
                      "variables":{"searchType":"AGENT","name":"a","country":"US","pagination":{"size":24,"from":0},"sort": None,},
                      "query":"fragment SearchResultFragment on SearchResult {  agents {    activeLocations {     city      state      __typename    }    asab    bio    cityState    email    facebook    firstName    id    lastName    linkedIn    phoneNumber    photo    state    stateBroker    preferredName    title    twitter    website    __typename  }  count  __typename}query SearchQuery($country: String, $location: String, $name: String, $pagination: Pagination, $searchType: SearchType!, $sort: Sort) {  search(    country: $country    location: $location    name: $name    pagination: $pagination    searchType: $searchType    sort: $sort  ) {    ...SearchResultFragment    __typename  }}"}


	def parse_link(self, url):
		print("inside parse")
		response = requests.post(url=url, data=json.dumps(self.payload), headers=self.headers)
		print(response.status_code)
		data = json.loads(response.text)
		for data in data['data']['search']['agents']:
			print(data)

url = "https://agentdir-api.showcaseidx.com/graphql"
exp = Exprealty()
try:
	exp.parse_link(url)
except:
	print("Error")
