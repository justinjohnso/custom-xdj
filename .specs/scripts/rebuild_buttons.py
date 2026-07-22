import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

settings_panel = """	<panel name="Settings_View" visible="var '$show_settings' 1">
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
			<pos x="650" y="100"/>
			<size width="300" height="40"/>
			<text format="EQ Mode" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="eq_mode 1" visible="eq_mode 0">
			<pos x="950" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="EQ" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="eq_mode 2" visible="eq_mode 1">
			<pos x="950" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="EZ MIX" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="eq_mode 3" visible="eq_mode 2">
			<pos x="950" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="STEMS" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="eq_mode 0" visible="eq_mode 3">
			<pos x="950" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="FILTER" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>

		<textzone>
			<pos x="1200" y="100"/>
			<size width="300" height="40"/>
			<text format="Start Recording" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="record on" visible="!record">
			<pos x="1500" y="100"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="REC" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="record off" visible="record">
			<pos x="1500" y="100"/>
			<size width="150" height="40"/>
			<off color="#ff3333" shape="square"/>
			<text format="RECORDING" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		
		<!-- Settings Options Row 2 -->
		<textzone>
			<pos x="150" y="160"/>
			<size width="300" height="40"/>
			<text format="Quantize" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="global_quantize on" visible="!global_quantize">
			<pos x="450" y="160"/>
			<size width="100" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="OFF" size="20" color="#aaaaaa" weight="bold" align="center"/>
		</button>
		<button action="global_quantize off" visible="global_quantize">
			<pos x="450" y="160"/>
			<size width="100" height="40"/>
			<off color="#0055ff" shape="square"/>
			<text format="ON" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>

		<textzone>
			<pos x="650" y="160"/>
			<size width="300" height="40"/>
			<text format="Needle Lock" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'needleLock' yes" visible="!setting 'needleLock'">
			<pos x="950" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="OFF" size="20" color="#aaaaaa" weight="bold" align="center"/>
		</button>
		<button action="setting 'needleLock' no" visible="setting 'needleLock'">
			<pos x="950" y="160"/>
			<size width="150" height="40"/>
			<off color="#0055ff" shape="square"/>
			<text format="ON" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>

		<textzone>
			<pos x="1200" y="160"/>
			<size width="300" height="40"/>
			<text format="Record Format" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'recordFormat' 'wav'" visible="setting 'recordFormat' 'mp3'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="MP3" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'recordFormat' 'flac'" visible="setting 'recordFormat' 'wav'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="WAV" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'recordFormat' 'ogg'" visible="setting 'recordFormat' 'flac'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="FLAC" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'recordFormat' 'mp4'" visible="setting 'recordFormat' 'ogg'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="OGG" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'recordFormat' 'webm'" visible="setting 'recordFormat' 'mp4'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="MP4" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'recordFormat' 'mp3'" visible="setting 'recordFormat' 'webm'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="WEBM" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<!-- Fallback if stuck in weird state -->
		<button action="setting 'recordFormat' 'mp3'" visible="!setting 'recordFormat' 'mp3' &amp; !setting 'recordFormat' 'wav' &amp; !setting 'recordFormat' 'flac' &amp; !setting 'recordFormat' 'ogg' &amp; !setting 'recordFormat' 'mp4' &amp; !setting 'recordFormat' 'webm'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="MP3" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		
		<!-- Settings Options Row 3 -->
		<textzone>
			<pos x="150" y="220"/>
			<size width="300" height="40"/>
			<text format="Slip Mode" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="slip_mode on" visible="!slip_mode">
			<pos x="450" y="220"/>
			<size width="100" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="OFF" size="20" color="#aaaaaa" weight="bold" align="center"/>
		</button>
		<button action="slip_mode off" visible="slip_mode">
			<pos x="450" y="220"/>
			<size width="100" height="40"/>
			<off color="#0055ff" shape="square"/>
			<text format="ON" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>

		<textzone>
			<pos x="650" y="220"/>
			<size width="300" height="40"/>
			<text format="Key Display" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'keyDisplay' 1" visible="setting 'keyDisplay' 0">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="MUSICAL" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'keyDisplay' 2" visible="setting 'keyDisplay' 1">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="CAMELOT" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'keyDisplay' 3" visible="setting 'keyDisplay' 2">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="OPENKEY" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'keyDisplay' 0" visible="setting 'keyDisplay' 3">
			<pos x="950" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="ALT" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>

		<textzone>
			<pos x="1200" y="220"/>
			<size width="300" height="40"/>
			<text format="Auto Record" size="24" color="#ffffff" align="left"/>
		</textzone>
		<button action="setting 'recordAutoStart' 1" visible="setting 'recordAutoStart' 0">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="OFF" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'recordAutoStart' 2" visible="setting 'recordAutoStart' 1">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#0055ff" shape="square"/>
			<text format="ON START" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
		<button action="setting 'recordAutoStart' 0" visible="setting 'recordAutoStart' 2">
			<pos x="1500" y="220"/>
			<size width="150" height="40"/>
			<off color="#0055ff" shape="square"/>
			<text format="ON PLAY" size="20" color="#ffffff" weight="bold" align="center"/>
		</button>
	</panel>"""

# Replace the entire Settings_View panel
xml = re.sub(r'<panel name="Settings_View".*?</panel>', settings_panel, xml, flags=re.DOTALL)

# Replace the EQ/Stems mode in the Performance view
mixer_eq_new = """<!-- EQ Mode Display & Toggle -->
		<textzone>
			<pos x="860" y="250"/>
			<size width="300" height="30"/>
			<text format="EQ / STEMS MODE" size="18" color="#888888" align="center"/>
		</textzone>
		<button action="eq_mode 1" visible="eq_mode 0">
			<pos x="860" y="280"/>
			<size width="300" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="EQ" size="24" color="#00ffcc" weight="bold" align="center"/>
		</button>
		<button action="eq_mode 2" visible="eq_mode 1">
			<pos x="860" y="280"/>
			<size width="300" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="EZ MIX" size="24" color="#00ffcc" weight="bold" align="center"/>
		</button>
		<button action="eq_mode 3" visible="eq_mode 2">
			<pos x="860" y="280"/>
			<size width="300" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="STEMS" size="24" color="#00ffcc" weight="bold" align="center"/>
		</button>
		<button action="eq_mode 0" visible="eq_mode 3">
			<pos x="860" y="280"/>
			<size width="300" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="FILTER" size="24" color="#00ffcc" weight="bold" align="center"/>
		</button>"""

xml = re.sub(r'<!-- EQ Mode Display & Toggle -->.*?</button>', mixer_eq_new, xml, flags=re.DOTALL)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

