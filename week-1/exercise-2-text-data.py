import json
from pprint import pprint

# json_file = open("reviews_automotive_5.json", "r")
# data = json.loads(json_file)
# print(data)



with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data)

