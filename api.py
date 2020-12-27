import requests
import json
from constants import *

s = requests.Session()

class API:
    def itemSearch(self, item):
        url = apiBase + f'item?q={item}&x-api-key={apiKey}'
        r = s.get(url)
        return r.json()

    def itemUIDSearch(self, UID):
        url = apiBase + f'item?uid={UID}&x-api-key={apiKey}'
        r = s.get(url)
        return r.json()

    def allItems(self):
        url = apiBase + f'items/all?x-api-key={apiKey}'
        r = s.get(url)
        return r.json()

    def BSGItems(self):
        url = apiBase + f'bsg/items/all?x-api-key={apiKey}'
        r = s.get(url)
        return r.json()