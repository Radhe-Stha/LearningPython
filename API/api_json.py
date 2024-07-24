import requests
import json

url = "https://jsonguide.technologychannel.org/quotes.json"

f = requests.get(url)
quotes = json.loads(f.text)


quotes_list = []

for quote in quotes:
    quotes_list.append(quote["text"])

for i in range(len(quotes_list)):
    quotes_list.append(quotes_list[i])


for i in range(len(quotes_list)):
    print(quotes_list[i])