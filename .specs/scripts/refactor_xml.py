with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Replace <panel> with <group>
xml = xml.replace('<panel name="Sidebar">', '<group name="Sidebar" x="0" y="0">')
xml = xml.replace('</panel>', '</group>')
xml = xml.replace('<panel visible="var \'$show_performance\' 1">', '<group visibility="var \'$show_performance\' 1">')
xml = xml.replace('<panel visible="var \'$show_browser\' 1">', '<group visibility="var \'$show_browser\' 1">')
xml = xml.replace('<panel visible="var \'$show_settings\' 1">', '<group visibility="var \'$show_settings\' 1">')
xml = xml.replace('<panel name="Performance_View" visible="var \'$show_performance\' 1">', '<group name="Performance_View" x="100" y="0" visibility="var \'$show_performance\' 1">')
xml = xml.replace('<panel name="Browser_View" visible="var \'$show_browser\' 1">', '<group name="Browser_View" x="100" y="0" visibility="var \'$show_browser\' 1">')
xml = xml.replace('<panel name="Mini_Decks">', '<group name="Mini_Decks" x="100" y="380">')

import re

# Adjust coords in Sidebar (base x=0, y=0, so coords stay same)
# Nothing to change

# Adjust coords in Performance_View (base x=100, y=0)
def shift_performance(m):
    block = m.group(0)
    block = re.sub(r'x="100"', 'x="0"', block)
    block = re.sub(r'x="1008"', 'x="908"', block) # center overlay 1008 - 100
    block = re.sub(r'x="1820"', 'x="1820"', block) # sizes stay same, just verifying not accidentally modifying widths if they matched
    return block

xml = re.sub(r'<group name="Performance_View" x="100" y="0" visibility="var \'\$show_performance\' 1">.*?</group>', shift_performance, xml, flags=re.DOTALL)

# Adjust coords in Browser_View (base x=100, y=0)
def shift_browser(m):
    block = m.group(0)
    block = re.sub(r'x="100"', 'x="0"', block)
    block = re.sub(r'x="110"', 'x="10"', block)
    return block
xml = re.sub(r'<group name="Browser_View" x="100" y="0" visibility="var \'\$show_browser\' 1">.*?</group>', shift_browser, xml, flags=re.DOTALL)

# Adjust coords in Mini_Decks (base x=100, y=380)
def shift_minidecks(m):
    block = m.group(0)
    # y coordinates: 380->0, 390->10, 440->60
    block = block.replace('y="380"', 'y="0"')
    block = block.replace('y="390"', 'y="10"')
    block = block.replace('y="440"', 'y="60"')
    
    # x coordinates: subtract 100
    def sub100(match):
        return f'x="{int(match.group(1)) - 100}"'
    block = re.sub(r'x="(\d+)"', sub100, block)
    
    # Re-fix sizes if they accidentally got caught (none of the sizes above match x="")
    return block

xml = re.sub(r'<group name="Mini_Decks" x="100" y="380">.*?</group>', shift_minidecks, xml, flags=re.DOTALL)

# Write output
with open("virtualdj-skin-modern.xml", "w") as f:
    f.write(xml)

