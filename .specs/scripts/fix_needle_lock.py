import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Replace Needle Lock text 
# needleLock appears to actually be a setting in VirtualDJ, but it's likely a simple boolean setting
# We'll explicitly check the text tag
n_old = re.search(r'<button action="setting \'needleLock\' \+1">.*?</button>', xml, re.DOTALL)
if n_old:
    n_new = """<button action="setting 'needleLock' +1">
			<pos x="950" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="ON" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'needleLock'" />
			<text format="OFF" size="20" color="#aaaaaa" weight="bold" align="center" visible="!setting 'needleLock'" />
		</button>"""
    xml = xml.replace(n_old.group(0), n_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

