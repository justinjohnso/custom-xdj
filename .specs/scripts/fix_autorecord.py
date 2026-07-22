import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

ra_old = re.search(r'<button action="setting \'recordAutoStart\' \+1">.*?</button>', xml, re.DOTALL)
if ra_old:
    ra_new = """<visual visible="setting 'recordAutoStart' 1">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#0055ff" shape="square"/>
		</visual>
		<visual visible="setting 'recordAutoStart' 2">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#0055ff" shape="square"/>
		</visual>
		<button action="setting 'recordAutoStart' +1">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="OFF" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordAutoStart' 0" />
			<text format="ON START" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordAutoStart' 1" />
			<text format="ON PLAY" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordAutoStart' 2" />
		</button>"""
    xml = xml.replace(ra_old.group(0), ra_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

