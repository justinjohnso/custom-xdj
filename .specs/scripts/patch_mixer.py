import re

with open("virtualdj-skin.xml", "r") as f:
    content = f.read()

mixer_content = """<!-- 3.3 Center/Mixer Info (Bottom Center) -->
		<visual>
			<pos x="750" y="240"/>
			<size width="520" height="140"/>
			<off color="#0a0a0a" shape="square"/>
		</visual>
		
		<!-- EQ Mode Display & Toggle -->
		<textzone>
			<pos x="860" y="250"/>
			<size width="300" height="30"/>
			<text format="EQ / STEMS MODE" size="18" color="#888888" align="center"/>
		</textzone>
		<button action="setting 'eqMode'">
			<pos x="860" y="280"/>
			<size width="300" height="40"/>
			<off color="#222222" shape="square"/>
			<text action="setting 'eqMode'" size="24" color="#00ffcc" weight="bold" align="center"/>
		</button>

		<!-- Crossfader -->
		<textzone>
			<pos x="860" y="330"/>
			<size width="300" height="20"/>
			<text format="CROSSFADER" size="14" color="#888888" align="center"/>
		</textzone>
		<slider action="crossfader">
			<pos x="860" y="350"/>
			<size width="300" height="20"/>
			<background color="#333333" shape="square"/>
			<thumb color="#ffffff" shape="square"/>
		</slider>
"""

new_content = re.sub(r'<!-- 3\.3 Center/Mixer Info \(Bottom Center\) -->.*?<!-- 3\.4 Deck 2 Info \(Bottom Right\) -->', mixer_content + '\n\t\t<!-- 3.4 Deck 2 Info (Bottom Right) -->', content, flags=re.DOTALL)

with open("virtualdj-skin.xml", "w") as f:
    f.write(new_content)

