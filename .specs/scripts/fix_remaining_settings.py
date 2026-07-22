import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Fix Needle Lock
n_old = re.search(r'<button action="setting \'needleLock\' \+1">.*?</button>', xml, re.DOTALL)
if n_old:
    n_new = """<button action="setting 'needleLock' +1">
			<pos x="950" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text action="setting 'needleLock'" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(n_old.group(0), n_new)

# Fix Record Format
rf_old = re.search(r'<button action="setting \'recordFormat\' \+1">.*?</button>', xml, re.DOTALL)
if rf_old:
    rf_new = """<button action="setting 'recordFormat' +1">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text action="setting 'recordFormat'" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(rf_old.group(0), rf_new)

# Fix Record Auto Start
ra_old = re.search(r'<button action="setting \'recordAutoStart\' \+1">.*?</button>', xml, re.DOTALL)
if ra_old:
    ra_new = """<button action="setting 'recordAutoStart' +1">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text action="setting 'recordAutoStart'" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(ra_old.group(0), ra_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

