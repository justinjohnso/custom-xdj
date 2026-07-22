import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

s_eq_old = re.search(r'<text format="EQ Mode".*?</button>', xml, re.DOTALL)
if s_eq_old:
    s_eq_new = """<text format="EQ Mode" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="eq_mode +1">
			<pos x="950" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="EQ" size="20" color="#ffffff" weight="bold" align="center" visible="eq_mode 0"/>
			<text format="EZ MIX" size="20" color="#ffffff" weight="bold" align="center" visible="eq_mode 1"/>
			<text format="STEMS" size="20" color="#ffffff" weight="bold" align="center" visible="eq_mode 2"/>
			<text format="FILTER" size="20" color="#ffffff" weight="bold" align="center" visible="eq_mode 3"/>
			<text format="STEMS" size="20" color="#ffffff" weight="bold" align="center" visible="eq_mode 4"/>
		</button>"""
    xml = xml.replace(s_eq_old.group(0), s_eq_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

