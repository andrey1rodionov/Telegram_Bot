import urllib.request

import json

# Openweathermap Weather codes and corressponding emojis
thunderstorm = u'\U0001F4A8'    # Code: 200's, 900, 901, 902, 905
drizzle = u'\U0001F4A7'         # Code: 300's
rain = u'\U00002614'            # Code: 500's
snowflake = u'\U00002744'       # Code: 600's snowflake
snowman = u'\U000026C4'         # Code: 600's snowman, 903, 906
atmosphere = u'\U0001F301'      # Code: 700's foogy
clearSky = u'\U00002600'        # Code: 800 clear sky
fewClouds = u'\U000026C5'       # Code: 801 sun behind clouds
clouds = u'\U00002601'          # Code: 802-803-804 clouds general
hot = u'\U0001F525'             # Code: 904
defaultEmoji = u'\U0001F300'    # default emojis

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
mist = parseResponse['main']['humidity']



temp_max = parseResponse['main']['temp_max']
temp_min = parseResponse['main']['temp_min']
cloud = parseResponse ['clouds']['all']
wind = parseResponse ['wind']['speed']
description_brief = parseResponse['weather'][0]['main']

weatherID = parseResponse['weather'][0]['main']


print(temp_min)
print(temp_max)
print(weather)
print(temperature)
print(mist)
print(cloud)
print(wind)
print(weatherID)