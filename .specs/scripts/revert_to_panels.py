import subprocess

# The user reported that moving to <group> broke the layout.
# Legacy VirtualDJ 8 specification heavily relied on <panel> for root-level views and absolute positioning.
# I will use git to revert virtualdj-skin.xml to exactly the commit before the group refactor,
# keeping the exact logic we verified worked, but then apply the stretching attribute.

subprocess.run(["git", "checkout", "HEAD~1", "--", "virtualdj-skin.xml"])
