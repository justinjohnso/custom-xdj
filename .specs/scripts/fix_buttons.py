import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Standardize inactive background colors for hardware-like buttons
xml = xml.replace('off color="#333333"', 'off color="#222222"')
xml = xml.replace('off color="#2a2a2a"', 'off color="#222222"')

# Fix Quantize
q_old = re.search(r'<button action="global_quantize">.*?</button>', xml, re.DOTALL)
if q_old:
    q_new = """<button action="global_quantize">
			<pos x="450" y="160"/>
			<size width="100" height="40"/>
			<off color="#222222" shape="square"/>
			<on color="#0055ff" shape="square"/>
			<text action="global_quantize ? 'ON' : 'OFF'" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(q_old.group(0), q_new)

# Fix Slip Mode
s_old = re.search(r'<button action="slip_mode">.*?</button>', xml, re.DOTALL)
if s_old:
    s_new = """<button action="slip_mode">
			<pos x="450" y="220"/>
			<size width="100" height="40"/>
			<off color="#222222" shape="square"/>
			<on color="#0055ff" shape="square"/>
			<text action="slip_mode ? 'ON' : 'OFF'" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(s_old.group(0), s_new)

# Make sure LOAD buttons have a slightly lighter background so they stand out
# We standardized to #222222 above, let's put LOAD back to #333333
load_btns = re.findall(r'<button action="load">.*?</button>', xml, re.DOTALL)
for btn in load_btns:
    new_btn = btn.replace('off color="#222222"', 'off color="#333333"')
    xml = xml.replace(btn, new_btn)

# Make REC button text dynamic
rec_old = re.search(r'<button action="record">.*?</button>', xml, re.DOTALL)
if rec_old:
    rec_new = """<button action="record">
			<pos x="1500" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<on color="#ff3333" shape="square"/>
			<text action="record ? 'RECORDING' : 'REC'" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>"""
    xml = xml.replace(rec_old.group(0), rec_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

