import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Quantize toggle fix
old_quantize = """<button action="global_quantize">
			<pos x="450" y="160"/>
			<size width="100" height="40"/>
			<off color="#333333" shape="square"/>
			<on color="#0055ff" shape="square"/>
			<text format="ON" size="20" color="#ffffff" align="center"/>
		</button>"""

new_quantize = """<button action="global_quantize">
			<pos x="450" y="160"/>
			<size width="100" height="40"/>
			<off color="#333333" shape="square"/>
			<on color="#0055ff" shape="square" visible="global_quantize"/>
			<text format="ON" size="20" color="#ffffff" align="center" visible="global_quantize"/>
			<text format="OFF" size="20" color="#aaaaaa" align="center" visible="!global_quantize"/>
		</button>"""
xml = xml.replace(old_quantize, new_quantize)

# Key Display cycle fix
old_key = """<button action="setting 'keyDisplay'">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#333333" shape="square"/>
			<text action="setting 'keyDisplay'" size="20" color="#ffffff" align="center"/>
		</button>"""

new_key = """<button action="setting 'keyDisplay' +1">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#333333" shape="square"/>
			<text action="setting 'keyDisplay'" size="20" color="#ffffff" align="center"/>
		</button>"""
xml = xml.replace(old_key, new_key)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

