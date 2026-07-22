import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Fix global_quantize text
q_old = re.search(r'<button action="global_quantize">.*?</button>', xml, re.DOTALL)
if q_old:
    q_new = """<button action="global_quantize">
			<pos x="450" y="160"/>
			<size width="100" height="40"/>
			<off color="#222222" shape="square"/>
			<on color="#0055ff" shape="square"/>
			<text format="ON" size="20" color="#ffffff" weight="bold" align="center" visible="global_quantize" />
			<text format="OFF" size="20" color="#aaaaaa" weight="bold" align="center" visible="!global_quantize" />
		</button>"""
    xml = xml.replace(q_old.group(0), q_new)

# Fix slip_mode text
s_old = re.search(r'<button action="slip_mode">.*?</button>', xml, re.DOTALL)
if s_old:
    s_new = """<button action="slip_mode">
			<pos x="450" y="220"/>
			<size width="100" height="40"/>
			<off color="#222222" shape="square"/>
			<on color="#0055ff" shape="square"/>
			<text format="ON" size="20" color="#ffffff" weight="bold" align="center" visible="slip_mode" />
			<text format="OFF" size="20" color="#aaaaaa" weight="bold" align="center" visible="!slip_mode" />
		</button>"""
    xml = xml.replace(s_old.group(0), s_new)

# Fix record text
r_old = re.search(r'<button action="record">.*?</button>', xml, re.DOTALL)
if r_old:
    r_new = """<button action="record">
			<pos x="1500" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<on color="#ff3333" shape="square"/>
			<text format="RECORDING" size="20" color="#ffffff" weight="bold" align="center" visible="record" />
			<text format="REC" size="20" color="#ffffff" weight="bold" align="center" visible="!record" />
		</button>"""
    xml = xml.replace(r_old.group(0), r_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

