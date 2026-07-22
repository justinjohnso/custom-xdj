import re

with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

pattern = re.compile(
    r'\s*<textzone>\s*<pos x="150" y="100"/>\s*<size width="300" height="40"/>\s*<text format="Show Pads \(Skin\)"[^>]*>\s*</textzone>\s*<button action="toggle \'\$show_pads\'">.*?</button>',
    re.DOTALL
)

xml = pattern.sub('', xml)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

