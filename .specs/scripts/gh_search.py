import urllib.request
import json
import os

url = "https://api.github.com/search/code?q=setting+key+extension:xml"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        for item in data.get('items', [])[:5]:
            print(item['repository']['full_name'], item['name'])
except Exception as e:
    print(e)
