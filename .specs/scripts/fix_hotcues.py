import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Replace Deck 1 and 2 Hotcues with Loop Cluster and Hotcues

deck1_old = re.search(r'<!-- 4 Hotcue buttons -->.*?</deck>', xml, re.DOTALL)
if deck1_old:
    deck1_new = """<!-- Loop Cluster -->
			<button action="loop_half">
				<pos x="210" y="300"/>
				<size width="60" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="1/2X" size="18" color="#ffffff" weight="bold" align="center"/>
			</button>
			<button action="loop">
				<pos x="280" y="300"/>
				<size width="80" height="40"/>
				<off color="#222222" shape="square"/>
				<on color="#ff9900" shape="square"/>
				<text format="LOOP" size="18" color="#ffffff" weight="bold" align="center"/>
			</button>
			<button action="loop_double">
				<pos x="370" y="300"/>
				<size width="60" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="2X" size="18" color="#ffffff" weight="bold" align="center"/>
			</button>

			<!-- 4 Hotcue buttons -->
			<button action="hot_cue 1">
				<pos x="450" y="300"/>
				<size width="40" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="1" size="20" color="#ff3333" weight="bold" align="center"/>
			</button>
			<button action="hot_cue 2">
				<pos x="500" y="300"/>
				<size width="40" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="2" size="20" color="#33ff33" weight="bold" align="center"/>
			</button>
			<button action="hot_cue 3">
				<pos x="550" y="300"/>
				<size width="40" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="3" size="20" color="#3333ff" weight="bold" align="center"/>
			</button>
			<button action="hot_cue 4">
				<pos x="600" y="300"/>
				<size width="40" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="4" size="20" color="#ffff33" weight="bold" align="center"/>
			</button>
		</deck>"""
    xml = xml.replace(deck1_old.group(0), deck1_new, 1)

deck2_old = re.search(r'<!-- 4 Hotcue buttons -->.*?</deck>', xml, re.DOTALL)
if deck2_old:
    deck2_new = """<!-- Loop Cluster -->
			<button action="loop_half">
				<pos x="1290" y="300"/>
				<size width="60" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="1/2X" size="18" color="#ffffff" weight="bold" align="center"/>
			</button>
			<button action="loop">
				<pos x="1360" y="300"/>
				<size width="80" height="40"/>
				<off color="#222222" shape="square"/>
				<on color="#ff9900" shape="square"/>
				<text format="LOOP" size="18" color="#ffffff" weight="bold" align="center"/>
			</button>
			<button action="loop_double">
				<pos x="1450" y="300"/>
				<size width="60" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="2X" size="18" color="#ffffff" weight="bold" align="center"/>
			</button>

			<!-- 4 Hotcue buttons -->
			<button action="hot_cue 1">
				<pos x="1530" y="300"/>
				<size width="40" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="1" size="20" color="#ff3333" weight="bold" align="center"/>
			</button>
			<button action="hot_cue 2">
				<pos x="1580" y="300"/>
				<size width="40" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="2" size="20" color="#33ff33" weight="bold" align="center"/>
			</button>
			<button action="hot_cue 3">
				<pos x="1630" y="300"/>
				<size width="40" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="3" size="20" color="#3333ff" weight="bold" align="center"/>
			</button>
			<button action="hot_cue 4">
				<pos x="1680" y="300"/>
				<size width="40" height="40"/>
				<off color="#222222" shape="square"/>
				<text format="4" size="20" color="#ffff33" weight="bold" align="center"/>
			</button>
		</deck>"""
    xml = xml.replace(deck2_old.group(0), deck2_new, 1)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)
