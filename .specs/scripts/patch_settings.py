import re

with open("virtualdj-skin.xml", "r") as f:
    content = f.read()

# I will replace the contents of Settings_View with a grid of real VDJ settings.

settings_content = """
	<panel name="Settings_View" visible="var '$show_settings' 1">
		<visual>
			<pos x="100" y="0"/>
			<size width="1820" height="380"/>
			<off color="#222222" shape="square"/>
		</visual>
		<textzone>
			<pos x="100" y="20"/>
			<size width="1820" height="60"/>
			<text format="OPTIONS &amp; SETTINGS" size="36" color="#ffffff" weight="bold" align="center"/>
		</textzone>
		
		<!-- Settings Options Row 1 -->
		<textzone>
			<pos x="150" y="100"/>
			<size width="300" height="40"/>
			<text format="Show Pads (Skin)" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="toggle '$show_pads'">
			<pos x="450" y="100"/>
			<size width="100" height="40"/>
			<off color="#333333" shape="square"/>
			<on color="#0055ff" shape="square" visible="var '$show_pads' 1"/>
			<text format="YES" size="20" color="#ffffff" align="center" visible="var '$show_pads' 1"/>
			<text format="NO" size="20" color="#aaaaaa" align="center" visible="var '$show_pads' 0"/>
		</button>
		
		<textzone>
			<pos x="650" y="100"/>
			<size width="300" height="40"/>
			<text format="EQ Mode" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'eqMode'">
			<pos x="950" y="100"/>
			<size width="150" height="40"/>
			<off color="#333333" shape="square"/>
			<text action="setting 'eqMode'" size="20" color="#ffffff" align="center"/>
		</button>

		<textzone>
			<pos x="1200" y="100"/>
			<size width="300" height="40"/>
			<text format="Start Recording" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="record">
			<pos x="1500" y="100"/>
			<size width="150" height="40"/>
			<off color="#333333" shape="square"/>
			<on color="#ff0000" shape="square"/>
			<text format="REC" size="20" color="#ffffff" align="center"/>
		</button>
		
		<!-- Settings Options Row 2 -->
		<textzone>
			<pos x="150" y="160"/>
			<size width="300" height="40"/>
			<text format="Quantize" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="global_quantize">
			<pos x="450" y="160"/>
			<size width="100" height="40"/>
			<off color="#333333" shape="square"/>
			<on color="#0055ff" shape="square"/>
			<text format="ON" size="20" color="#ffffff" align="center"/>
		</button>

		<textzone>
			<pos x="650" y="160"/>
			<size width="300" height="40"/>
			<text format="Needle Lock" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'needleLock'">
			<pos x="950" y="160"/>
			<size width="150" height="40"/>
			<off color="#333333" shape="square"/>
			<text action="setting 'needleLock'" size="20" color="#ffffff" align="center"/>
		</button>

		<textzone>
			<pos x="1200" y="160"/>
			<size width="300" height="40"/>
			<text format="Record Format" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'recordFormat'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#333333" shape="square"/>
			<text action="setting 'recordFormat'" size="20" color="#ffffff" align="center"/>
		</button>
		
		<!-- Settings Options Row 3 -->
		<textzone>
			<pos x="150" y="220"/>
			<size width="300" height="40"/>
			<text format="Slip Mode" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="slip_mode">
			<pos x="450" y="220"/>
			<size width="100" height="40"/>
			<off color="#333333" shape="square"/>
			<on color="#0055ff" shape="square"/>
			<text format="ON" size="20" color="#ffffff" align="center"/>
		</button>

		<textzone>
			<pos x="650" y="220"/>
			<size width="300" height="40"/>
			<text format="Key Display" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'keyDisplay'">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#333333" shape="square"/>
			<text action="setting 'keyDisplay'" size="20" color="#ffffff" align="center"/>
		</button>

		<textzone>
			<pos x="1200" y="220"/>
			<size width="300" height="40"/>
			<text format="Auto Record" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'recordAutoStart'">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#333333" shape="square"/>
			<text action="setting 'recordAutoStart'" size="20" color="#ffffff" align="center"/>
		</button>
	</panel>
"""

new_content = re.sub(r'<panel name="Settings_View".*?</panel>', settings_content, content, flags=re.DOTALL)

with open("virtualdj-skin.xml", "w") as f:
    f.write(new_content)

