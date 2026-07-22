import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

sidebar_match = re.search(r'<panel name="Sidebar">.*?</panel>', xml, re.DOTALL)
if sidebar_match:
    sidebar = sidebar_match.group(0)
    
    # Simple replace logic since regex was tripping up on ampersands inside the button tags
    sidebar = re.sub(
        r'<!-- Performance Button -->.*?<button action="set \'\$show_performance\' 1 &amp; set \'\$show_browser\' 0 &amp; set \'\$show_settings\' 0">.*?<pos x="10" y="80"/>.*?<size width="80" height="80"/>.*?<off color="#222222" shape="square"/>.*?<on color="#0055ff" shape="square" visible="var \'\$show_performance\' 1"/>.*?<text format="PERFORM" align="center" color="#ffffff" size="14" weight="bold" />.*?</button>',
        """<!-- Performance Button -->
		<visual visible="var '$show_performance' 0">
			<pos x="10" y="80"/>
			<size width="80" height="80"/>
			<off color="#222222" shape="square"/>
		</visual>
		<visual visible="var '$show_performance' 1">
			<pos x="10" y="80"/>
			<size width="80" height="80"/>
			<off color="#0055ff" shape="square"/>
		</visual>
		<button action="set '$show_performance' 1 &amp; set '$show_browser' 0 &amp; set '$show_settings' 0">
			<pos x="10" y="80"/>
			<size width="80" height="80"/>
			<text format="PERFORM" align="center" color="#ffffff" size="14" weight="bold" />
		</button>""", sidebar, flags=re.DOTALL)

    sidebar = re.sub(
        r'<!-- Browser Button -->.*?<button action="set \'\$show_performance\' 0 &amp; set \'\$show_browser\' 1 &amp; set \'\$show_settings\' 0">.*?<pos x="10" y="180"/>.*?<size width="80" height="80"/>.*?<off color="#222222" shape="square"/>.*?<on color="#0055ff" shape="square" visible="var \'\$show_browser\' 1"/>.*?<text format="BROWSE" align="center" color="#ffffff" size="14" weight="bold" />.*?</button>',
        """<!-- Browser Button -->
		<visual visible="var '$show_browser' 0">
			<pos x="10" y="180"/>
			<size width="80" height="80"/>
			<off color="#222222" shape="square"/>
		</visual>
		<visual visible="var '$show_browser' 1">
			<pos x="10" y="180"/>
			<size width="80" height="80"/>
			<off color="#0055ff" shape="square"/>
		</visual>
		<button action="set '$show_performance' 0 &amp; set '$show_browser' 1 &amp; set '$show_settings' 0">
			<pos x="10" y="180"/>
			<size width="80" height="80"/>
			<text format="BROWSE" align="center" color="#ffffff" size="14" weight="bold" />
		</button>""", sidebar, flags=re.DOTALL)

    sidebar = re.sub(
        r'<!-- Settings Button -->.*?<button action="set \'\$show_performance\' 0 &amp; set \'\$show_browser\' 0 &amp; set \'\$show_settings\' 1">.*?<pos x="10" y="280"/>.*?<size width="80" height="80"/>.*?<off color="#222222" shape="square"/>.*?<on color="#0055ff" shape="square" visible="var \'\$show_settings\' 1"/>.*?<text format="SETTINGS" align="center" color="#ffffff" size="14" weight="bold" />.*?</button>',
        """<!-- Settings Button -->
		<visual visible="var '$show_settings' 0">
			<pos x="10" y="280"/>
			<size width="80" height="80"/>
			<off color="#222222" shape="square"/>
		</visual>
		<visual visible="var '$show_settings' 1">
			<pos x="10" y="280"/>
			<size width="80" height="80"/>
			<off color="#0055ff" shape="square"/>
		</visual>
		<button action="set '$show_performance' 0 &amp; set '$show_browser' 0 &amp; set '$show_settings' 1">
			<pos x="10" y="280"/>
			<size width="80" height="80"/>
			<text format="SETTINGS" align="center" color="#ffffff" size="14" weight="bold" />
		</button>""", sidebar, flags=re.DOTALL)

    sidebar = re.sub(
        r'<!-- System Settings Button -->.*?<button action="settings">.*?<pos x="10" y="380"/>.*?<size width="80" height="80"/>.*?<off color="#222222" shape="square"/>.*?<text format="SYSTEM" align="center" color="#ffffff" size="14" weight="bold" />.*?</button>',
        """<!-- System Settings Button -->
		<visual>
			<pos x="10" y="380"/>
			<size width="80" height="80"/>
			<off color="#3a3a3a" shape="square"/>
		</visual>
		<button action="settings">
			<pos x="10" y="380"/>
			<size width="80" height="80"/>
			<text format="SYSTEM" align="center" color="#ffffff" size="14" weight="bold" />
		</button>""", sidebar, flags=re.DOTALL)

    xml = xml.replace(sidebar_match.group(0), sidebar)

mini_decks_match = re.search(r'<!-- Mini-Decks Panel \(Always Visible\) -->.*?</Skin>', xml, re.DOTALL)
if mini_decks_match:
    mini_decks = mini_decks_match.group(0)
    mini_decks = re.sub(
        r'<waveform>\s*<pos (x="\d+" y="\d+")/>\s*<size (width="\d+" height="\d+")/>\s*<colors (color="[^"]+" pos="[^"]+")/>\s*</waveform>',
        r'<songpos>\n\t\t\t\t<pos \1/>\n\t\t\t\t<size \2/>\n\t\t\t\t<colors \3/>\n\t\t\t</songpos>', 
        mini_decks, flags=re.DOTALL)
    xml = xml.replace(mini_decks_match.group(0), mini_decks)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

