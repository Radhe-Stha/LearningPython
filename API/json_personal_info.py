import json
import requests

#url = "https://jsonguide.technologychannel.org/info.json"
url = {
    'name':'ram',
    'age':'12',
    'place':'kathmandu'
}
#f = requests.get(url)
person_info = json.dumps(url)
print(person_info)

#info_list = []
#for info in person_info:
 #   info_list.append(info)
 #   print(info_list)