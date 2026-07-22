import urllib.request
import urllib.parse
import re

url = "https://lite.duckduckgo.com/lite/"
data = urllib.parse.urlencode({'q': 'virtualdj script "record_format"'}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    for s in re.findall(r'<td class=\'snippet\'>(.*?)</td>', html, re.IGNORECASE | re.DOTALL):
        print(re.sub(r'<[^>]+>', '', s).strip())
except Exception as e: print(e)
