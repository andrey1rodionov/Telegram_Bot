import urllib.request

import json

api_endpoint = "http://www.nbrb.by/API/ExRates"

url = api_endpoint + "/Rates?Periodicity=0"

response = urllib.request.urlopen(url)
parseResponse = json.loads(response.read())

USD = parseResponse[4]
EUR = parseResponse[5]
RUB = parseResponse[16]