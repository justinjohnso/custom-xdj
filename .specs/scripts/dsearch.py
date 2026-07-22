import urllib.request
import urllib.parse
import re

url = "https://lite.duckduckgo.com/lite/"
data = urllib.parse.urlencode({'q': 'site:virtualdj.com/forums "recordFormat"'}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
for s in re.findall(r'<td class=\'snippet\'>(.*?)</td>', html, re.IGNORECASE | re.DOTALL):
    print(re.sub(r'<[^>]+>', '', s).strip())
