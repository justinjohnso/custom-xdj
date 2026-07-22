import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Fix EQ Mode in settings
s_eq_old = re.search(r'<button action="setting \'eqMode\' \+1">.*?<text format="CYCLE".*?</button>', xml, re.DOTALL)
if s_eq_old:
    s_eq_new = """<button action="eq_mode +1">
			<pos x="950" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text action="eq_mode" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(s_eq_old.group(0), s_eq_new)

# Fix EQ Mode in Center Mixer
m_eq_old = re.search(r'<button action="setting \'eqMode\' \+1">.*?<text format="CYCLE".*?</button>', xml, re.DOTALL)
if m_eq_old:
    m_eq_new = """<button action="eq_mode +1">
			<pos x="860" y="280"/>
			<size width="300" height="40"/>
			<off color="#222222" shape="square"/>
			<text action="eq_mode" size="24" color="#00ffcc" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(m_eq_old.group(0), m_eq_new)

# Fix Key Display
# Using "setting 'keyDisplay' +1" and reading the setting value
k_old = re.search(r'<button action="setting \'keyDisplay\' \+1">.*?<text format="CYCLE".*?</button>', xml, re.DOTALL)
if k_old:
    k_new = """<button action="setting 'keyDisplay' +1">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text action="setting 'keyDisplay'" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(k_old.group(0), k_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

