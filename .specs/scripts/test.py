import urllib.request
import re

html = urllib.request.urlopen("https://www.virtualdj.com/wiki/VDJscript_Verbs.html").read().decode("utf-8")
print(len(re.findall("stem", html, re.IGNORECASE)))
