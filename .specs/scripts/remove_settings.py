import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# 1. Remove the Settings_View panel
xml = re.sub(r'\s*<!-- Phase 5: Settings View -->\s*<panel name="Settings_View".*?</panel>', '', xml, flags=re.DOTALL)

# 2. Remove settings button from Sidebar
xml = re.sub(r'\s*<!-- Settings Button -->.*?<!-- System Settings Button -->', '\n\n\t\t<!-- System Settings Button -->', xml, flags=re.DOTALL)

# 3. Clean up the set '$show_settings' state actions
xml = xml.replace(" &amp; set '$show_settings' 0", "")
xml = xml.replace(" &amp; set '$show_settings' 1", "")

# 4. Move System button up to y=280
sys_vis_old = r'<visual>\s*<pos x="10" y="380"/>\s*<size width="80" height="80"/>\s*<off color="#3a3a3a" shape="square"/>\s*</visual>'
sys_vis_new = r'''<visual>
			<pos x="10" y="280"/>
			<size width="80" height="80"/>
			<off color="#3a3a3a" shape="square"/>
		</visual>'''
xml = re.sub(sys_vis_old, sys_vis_new, xml, flags=re.DOTALL)

sys_btn_old = r'<button action="settings">\s*<pos x="10" y="380"/>\s*<size width="80" height="80"/>\s*<text format="SYSTEM" align="center" color="#ffffff" size="14" weight="bold" />\s*</button>'
sys_btn_new = r'''<button action="settings">
			<pos x="10" y="280"/>
			<size width="80" height="80"/>
			<text format="SYSTEM" align="center" color="#ffffff" size="14" weight="bold" />
		</button>'''
xml = re.sub(sys_btn_old, sys_btn_new, xml, flags=re.DOTALL)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

