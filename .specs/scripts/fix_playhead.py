import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Fix Deck 1 Overlay
deck1_wave_old = re.search(r'<scratchwave deck="left" orientation="horizontal">.*?</scratchwave>', xml, re.DOTALL)
if deck1_wave_old:
    deck1_wave_new = re.sub(
        r'<overlay>.*?<pos x="\d+" y="\d+"/>.*?<size width="\d+" height="\d+"/>.*?<background color="#ff3333" shape="square"/>.*?</overlay>',
        """<overlay>
				<pos x="1008" y="0"/>
				<size width="4" height="190"/>
				<background color="#ff3333" shape="square"/>
			</overlay>""",
        deck1_wave_old.group(0),
        flags=re.DOTALL
    )
    xml = xml.replace(deck1_wave_old.group(0), deck1_wave_new)

# Fix Deck 2 Overlay
deck2_wave_old = re.search(r'<scratchwave deck="right" orientation="horizontal">.*?</scratchwave>', xml, re.DOTALL)
if deck2_wave_old:
    deck2_wave_new = re.sub(
        r'<overlay>.*?<pos x="\d+" y="\d+"/>.*?<size width="\d+" height="\d+"/>.*?<background color="#ff3333" shape="square"/>.*?</overlay>',
        """<overlay>
				<pos x="1008" y="190"/>
				<size width="4" height="190"/>
				<background color="#ff3333" shape="square"/>
			</overlay>""",
        deck2_wave_old.group(0),
        flags=re.DOTALL
    )
    xml = xml.replace(deck2_wave_old.group(0), deck2_wave_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

