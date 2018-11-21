import urllib.request

import json

api_endpoint = "http://www.nbrb.by/API/ExRates"

url = api_endpoint + "/Rates?Periodicity=0"

response = urllib.request.urlopen(url)
parseResponse = json.loads(response.read())

UAH = parseResponse[2]
USD = parseResponse[4]
EUR = parseResponse[5]
PLN = parseResponse[6]
BGN = parseResponse[1]
RUB = parseResponse[16]
GBP = parseResponse[22]


print(USD['Cur_OfficialRate'])
