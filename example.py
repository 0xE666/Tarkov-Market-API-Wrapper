import requests
import json
from constants import *
import api


t = api.API()

#item Name Search
search = t.itemSearch('BTC')

#item UID Search
UIDSearch = t.itemUIDSearch('5ac84494-465a-424a-b36e-fe22869ba5ec')

#all items dump
f = open("allItems.txt", "w+")
f.write(json.dumps(t.allItems(), indent=4))
f.close()

#RAW BSG all items dump
f = open("BSGItems.txt", "w+")
f.write(json.dumps(t.BSGItems(), indent=4))
f.close()


currency = '₽'
itemUID = search[0]['uid']
itemName = search[0]['name']
itemShortName = search[0]['shortName']
itemPrice = search[0]['price']
item24HPrice = search[0]['avg24hPrice']
item7DPrice = search[0]['avg7daysPrice']
traderName = search[0]['traderName']
traderPrice = search[0]['traderPrice']
wikiLink = search[0]['wikiLink']
icon = search[0]['icon']

