import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

s_eq_old = re.search(r'<text format="EQ Mode" size="24" color="#ffffff" align="left"/>\s*</textzone>\s*<button action="eq_mode \+1">\s*<pos x="\d+" y="\d+"/>.*?<off color="#222222" shape="square"/>\s*<text action="eq_mode"[^>]*>\s*</button>', xml, re.DOTALL)
if s_eq_old:
    print("Found eqMode in Settings")
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

# In the previous python script I accidentally replaced the wrong one or matched something weirdly. Let's fix the Center Mixer one just in case the coordinates got messed up.
# Wait, the previous script replaced `<button action="eq_mode +1">.*?<text action="eq_mode".*?</button>` which matched the FIRST one it found (which was the settings one, but it put the coordinates of the mixer one: x=860 y=280).
# Let's completely restore the Settings one and the Mixer one.

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

