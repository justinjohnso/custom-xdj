import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Fix Record button
r_old = re.search(r'<button action="record">.*?</button>', xml, re.DOTALL)
if r_old:
    r_new = """<visual visible="!record">
			<pos x="1500" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
		</visual>
		<visual visible="record">
			<pos x="1500" y="100"/>
			<size width="150" height="40"/>
			<off color="#ff3333" shape="square"/>
		</visual>
		<button action="record">
			<pos x="1500" y="100"/>
			<size width="150" height="40"/>
			<text format="RECORDING" size="20" color="#ffffff" weight="bold" align="center" visible="record" />
			<text format="REC" size="20" color="#ffffff" weight="bold" align="center" visible="!record" />
		</button>"""
    xml = xml.replace(r_old.group(0), r_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

