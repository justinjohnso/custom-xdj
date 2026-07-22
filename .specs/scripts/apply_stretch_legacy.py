import subprocess
import re

# 1. We must fully revert the bad commit (687e9fc) that broke the layout.
subprocess.run(["git", "revert", "--no-commit", "HEAD"])

# 2. Now read the reverted file and apply the stretch tag.
with open("virtualdj-skin.xml", "r") as f:
    xml = f.read()

# Make the skin stretchable to 100% width and height so it scales gracefully on laptop
xml = re.sub(
    r'<Skin name="XDJ 480 Hardware" version="8" width="1920" height="480" nbdecks="2" image="2Decks.png">',
    r'<Skin name="XDJ 480 Hardware" version="8" width="1920" height="480" stretch="yes" ratio="none" nbdecks="2" image="2Decks.png">',
    xml
)

with open("virtualdj-skin.xml", "w") as f:
    f.write(xml)

