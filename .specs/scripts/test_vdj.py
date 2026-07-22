import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Fix EQ Mode
m_eq_old = re.search(r'<button action="eq_mode \+1">.*?<text action="eq_mode".*?</button>', xml, re.DOTALL)
if m_eq_old:
    m_eq_new = """<button action="eq_mode +1">
			<pos x="860" y="280"/>
			<size width="300" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="EQ" size="24" color="#00ffcc" weight="bold" align="center" visible="eq_mode 0"/>
			<text format="EZ MIX" size="24" color="#00ffcc" weight="bold" align="center" visible="eq_mode 1"/>
			<text format="STEMS" size="24" color="#00ffcc" weight="bold" align="center" visible="eq_mode 2"/>
			<text format="FILTER" size="24" color="#00ffcc" weight="bold" align="center" visible="eq_mode 3"/>
			<text format="STEMS" size="24" color="#00ffcc" weight="bold" align="center" visible="eq_mode 4"/>
		</button>"""
    xml = xml.replace(m_eq_old.group(0), m_eq_new)

# Fix Key Display
k_old = re.search(r'<button action="setting \'keyDisplay\' \+1">.*?<text action="setting \'keyDisplay\'".*?</button>', xml, re.DOTALL)
if k_old:
    k_new = """<button action="setting 'keyDisplay' +1">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="MUSICAL" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'keyDisplay' 0" />
			<text format="CAMELOT" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'keyDisplay' 1" />
			<text format="OPENKEY" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'keyDisplay' 2" />
			<text format="ALT" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'keyDisplay' 3" />
		</button>"""
    xml = xml.replace(k_old.group(0), k_new)
    
# Fix Record Format
rf_old = re.search(r'<button action="setting \'recordFormat\' \+1">.*?<text action="setting \'recordFormat\'".*?</button>', xml, re.DOTALL)
if rf_old:
    rf_new = """<button action="setting 'recordFormat' +1">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="MP3" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 0" />
			<text format="OGG" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 1" />
			<text format="FLAC" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 2" />
			<text format="WAV" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 3" />
			<text format="MP4" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 4" />
			<text format="WEBM" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 5" />
		</button>"""
    xml = xml.replace(rf_old.group(0), rf_new)
    
# Fix Auto Record
ra_old = re.search(r'<button action="setting \'recordAutoStart\' \+1">.*?<text action="setting \'recordAutoStart\'".*?</button>', xml, re.DOTALL)
if ra_old:
    ra_new = """<button action="setting 'recordAutoStart' +1">
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

