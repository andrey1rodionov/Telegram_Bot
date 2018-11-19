import urllib.request

import json

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

city = "London"

# Replace with your API KEY
apikey = "cdcd96e5ab88f6059051a3671507b237"

# Put all the components of the URL together
url = api_endpoint + "?q=" + city + "&appid=" + apikey

response = urllib.request.urlopen(url)
parseResponse = json.loads(response.read())

temperature = parseResponse['main']['temp']
weather = parseResponse['weather'][0]['description']

print (temperature)
print (weather)