import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

mixer_match = re.search(r'<!-- 3\.3 Center/Mixer Info \(Bottom Center\) -->.*?<!-- 3\.4 Deck 2 Info \(Bottom Right\) -->', xml, re.DOTALL)
if mixer_match:
    mixer_old = mixer_match.group(0)
    mixer_new = """<!-- 3.3 Center/Mixer Info (Bottom Center) -->
		<visual>
			<pos x="750" y="240"/>
			<size width="520" height="140"/>
			<off color="#0a0a0a" shape="square"/>
		</visual>
		
		<!-- Zoom Controls -->
		<button action="zoom -1">
			<pos x="760" y="250"/>
			<size width="40" height="30"/>
			<off color="#222222" shape="square"/>
			<text format="-" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="zoom +1">
			<pos x="810" y="250"/>
			<size width="40" height="30"/>
			<off color="#222222" shape="square"/>
			<text format="+" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>

		<!-- Deck 1 EQ & Stems -->
		<slider action="eq_high" orientation="vertical">
			<pos x="880" y="250"/>
			<size width="20" height="100"/>
			<background color="#333333" shape="square"/>
			<thumb color="#ffffff" shape="square"/>
		</slider>
		<slider action="eq_mid" orientation="vertical">
			<pos x="910" y="250"/>
			<size width="20" height="100"/>
			<background color="#333333" shape="square"/>
			<thumb color="#ffffff" shape="square"/>
		</slider>
		<slider action="eq_low" orientation="vertical">
			<pos x="940" y="250"/>
			<size width="20" height="100"/>
			<background color="#333333" shape="square"/>
			<thumb color="#ffffff" shape="square"/>
		</slider>
		<slider action="stem 'vocal'" orientation="vertical">
			<pos x="980" y="250"/>
			<size width="20" height="100"/>
			<background color="#442222" shape="square"/>
			<thumb color="#ff3333" shape="square"/>
		</slider>
		<slider action="stem 'inst'" orientation="vertical">
			<pos x="1010" y="250"/>
			<size width="20" height="100"/>
			<background color="#222244" shape="square"/>
			<thumb color="#3333ff" shape="square"/>
		</slider>
		<slider action="stem 'beat'" orientation="vertical">
			<pos x="1040" y="250"/>
			<size width="20" height="100"/>
			<background color="#224422" shape="square"/>
			<thumb color="#33ff33" shape="square"/>
		</slider>
		
		<!-- Deck 2 Stems & EQ -->
		<slider action="stem 'beat'" orientation="vertical">
			<pos x="1080" y="250"/>
			<size width="20" height="100"/>
			<background color="#224422" shape="square"/>
			<thumb color="#33ff33" shape="square"/>
		</slider>
		<slider action="stem 'inst'" orientation="vertical">
			<pos x="1110" y="250"/>
			<size width="20" height="100"/>
			<background color="#222244" shape="square"/>
			<thumb color="#3333ff" shape="square"/>
		</slider>
		<slider action="stem 'vocal'" orientation="vertical">
			<pos x="1140" y="250"/>
			<size width="20" height="100"/>
			<background color="#442222" shape="square"/>
			<thumb color="#ff3333" shape="square"/>
		</slider>
		<slider action="eq_low" orientation="vertical">
			<pos x="1180" y="250"/>
			<size width="20" height="100"/>
			<background color="#333333" shape="square"/>
			<thumb color="#ffffff" shape="square"/>
		</slider>
		<slider action="eq_mid" orientation="vertical">
			<pos x="1210" y="250"/>
			<size width="20" height="100"/>
			<background color="#333333" shape="square"/>
			<thumb color="#ffffff" shape="square"/>
		</slider>
		<slider action="eq_high" orientation="vertical">
			<pos x="1240" y="250"/>
			<size width="20" height="100"/>
			<background color="#333333" shape="square"/>
			<thumb color="#ffffff" shape="square"/>
		</slider>

		<!-- 3.4 Deck 2 Info (Bottom Right) -->"""
    xml = xml.replace(mixer_old, mixer_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

