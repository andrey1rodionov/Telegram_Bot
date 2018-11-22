import urllib.request

import json

api_endpoint = "https://newsapi.org/v2/top-headlines?sources=google-news-ru"

apikey = "ee793d3a00ff404780cad47b8967013e"

news_url = api_endpoint + "&apiKey=" + apikey

response = urllib.request.urlopen(news_url)

news_now = json.loads(response.read())
