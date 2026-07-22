import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Fix keyDisplay text
k_old = re.search(r'<button action="setting \'keyDisplay\' \+1">.*?</button>', xml, re.DOTALL)
if k_old:
    k_new = """<button action="setting 'keyDisplay' +1">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="CYCLE" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(k_old.group(0), k_new)

# Fix eqMode text
e_old = re.search(r'<button action="setting \'eqMode\'">.*?</button>', xml, re.DOTALL)
if e_old:
    e_new = """<button action="setting 'eqMode' +1">
			<pos x="950" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="CYCLE" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(e_old.group(0), e_new)

# Fix needleLock text
n_old = re.search(r'<button action="setting \'needleLock\'">.*?</button>', xml, re.DOTALL)
if n_old:
    n_new = """<button action="setting 'needleLock' +1">
			<pos x="950" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="CYCLE" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(n_old.group(0), n_new)

# Fix recordFormat text
rf_old = re.search(r'<button action="setting \'recordFormat\'">.*?</button>', xml, re.DOTALL)
if rf_old:
    rf_new = """<button action="setting 'recordFormat' +1">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="CYCLE" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(rf_old.group(0), rf_new)

# Fix recordAutoStart text
ra_old = re.search(r'<button action="setting \'recordAutoStart\'">.*?</button>', xml, re.DOTALL)
if ra_old:
    ra_new = """<button action="setting 'recordAutoStart' +1">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="CYCLE" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(ra_old.group(0), ra_new)


with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

