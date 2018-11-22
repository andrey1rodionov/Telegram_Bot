import json
import urllib.error
import urllib.request

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

# Replace with your API KEY
apikey = "cdcd96e5ab88f6059051a3671507b237"

# Openweathermap Weather codes and corressponding emojis
thunderstorm = u'\U0001F4A8'  # Code: 200's, 900, 901, 902, 905
drizzle = u'\U0001F4A7'  # Code: 300's
rain = u'\U00002614'  # Code: 500's
snowflake = u'\U00002744'  # Code: 600's snowflake
snowman = u'\U000026C4'  # Code: 600's snowman, 903, 906
atmosphere = u'\U0001F301'  # Code: 700's foogy
clearSky = u'\U00002600'  # Code: 800 clear sky
fewClouds = u'\U000026C5'  # Code: 801 sun behind clouds
clouds = u'\U00002601'  # Code: 802-803-804 clouds general
hot = u'\U0001F525'  # Code: 904
defaultEmoji = u'\U0001F300'  # default emojis

degree_sign = u'\N{DEGREE SIGN}'


def get_weather_for_specific_city(city):
    city_url = api_endpoint + "?q=" + city + "&appid=" + apikey
    try:
        resp = urllib.request.urlopen(city_url)
        parsed_resp = json.loads(resp.read())

        weather = parsed_resp['weather'][0]['description']
        temperature = parsed_resp['main']['temp']
        temp_max = parsed_resp['main']['temp_max']
        temp_min = parsed_resp['main']['temp_min']
        cloud = parsed_resp['clouds']['all']
        wind = parsed_resp['wind']['speed']
        humidity = parsed_resp['main']['humidity']

        message = str(weather) + \
                  "\n" + 'Temperature now ' + str(round(temperature - 273.15)) + ' ' + degree_sign + 'С' + \
                  "\n" + 'Temperature from ' + str(round(temp_min - 273.15)) + \
                  ' to ' + str(round(temp_max - 273.15)) + ' ' + degree_sign + 'С' + \
                  "\n" + 'Wind ' + str(wind) + ' m/s ' + \
                  "\n" + 'Humidity ' + str(humidity) + ' % ' + \
                  "\n" + 'Clouds ' + str(cloud) + ' % '

    except urllib.error.HTTPError as err:
        if err.code == 404:
            message = 'Такого города не существует'
        else:
            message = 'Ошибка'

    return message
