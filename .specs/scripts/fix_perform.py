import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Replace Performance View panel entirely
perform_match = re.search(r'<!-- Phase 3: Main Performance View -->.*?<!-- Phase 4: Browser View -->', xml, re.DOTALL)
if perform_match:
    new_perform = """<!-- Phase 3: Main Performance View -->
	<panel name="Performance_View" visible="var '$show_performance' 1">
		<visual>
			<pos x="100" y="0"/>
			<size width="1820" height="380"/>
			<off color="#050505" shape="square"/>
		</visual>

		<!-- Waveforms (Maximized) -->
		<scratchwave deck="left" orientation="horizontal">
			<pos x="100" y="0"/>
			<size width="1820" height="190"/>
			<grid color="#555555" height="10" size="1" mainsize="4" mirrored="true"/>
			<gridlines color="#333333" width="1" transparency="0.5"/>
			<overlay>
				<pos x="908" y="0"/>
				<size width="4" height="190"/>
				<background color="#ff3333" shape="square"/>
			</overlay>
		</scratchwave>

		<scratchwave deck="right" orientation="horizontal">
			<pos x="100" y="190"/>
			<size width="1820" height="190"/>
			<grid color="#555555" height="10" size="1" mainsize="4" mirrored="true"/>
			<gridlines color="#333333" width="1" transparency="0.5"/>
			<overlay>
				<pos x="908" y="0"/>
				<size width="4" height="190"/>
				<background color="#ff3333" shape="square"/>
			</overlay>
		</scratchwave>
	</panel>

	<!-- Phase 4: Browser View -->"""
    xml = xml.replace(perform_match.group(0), new_perform)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

