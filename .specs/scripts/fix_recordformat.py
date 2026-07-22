import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

rf_old = re.search(r'<button action="setting \'recordFormat\' \+1">.*?</button>', xml, re.DOTALL)
if rf_old:
    rf_new = """<button action="setting 'recordFormat' 'mp3' ? setting 'recordFormat' 'wav' : setting 'recordFormat' 'wav' ? setting 'recordFormat' 'flac' : setting 'recordFormat' 'flac' ? setting 'recordFormat' 'ogg' : setting 'recordFormat' 'mp3'">
			<pos x="1500" y="160"/>
			<size width="150" height="40"/>
			<off color="#222222" shape="square"/>
			<text format="MP3" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 'mp3'" />
			<text format="WAV" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 'wav'" />
			<text format="FLAC" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 'flac'" />
			<text format="OGG" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 'ogg'" />
			<text format="MP4" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 'mp4'" />
			<text format="WEBM" size="20" color="#ffffff" weight="bold" align="center" visible="setting 'recordFormat' 'webm'" />
		</button>"""
    xml = xml.replace(rf_old.group(0), rf_new)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

