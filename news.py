import urllib.request

import json

api_endpoint_ru = "http://newsapi.org/v2/top-headlines?sources=google-news-ru"

api_endpoint_eng = "http://newsapi.org/v2/top-headlines?sources=google-news"

apikey = "ee793d3a00ff404780cad47b8967013e"

news_url_ru = api_endpoint_ru + "&apiKey=" + apikey

news_url_eng = api_endpoint_eng + "&apiKey=" + apikey

response_ru = urllib.request.urlopen(news_url_ru)

response_eng = urllib.request.urlopen(news_url_eng)

news_now_ru = json.loads(response_ru.read())

news_now_eng = json.loads(response_eng.read())
