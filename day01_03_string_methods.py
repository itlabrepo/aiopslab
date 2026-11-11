version_raw = "  Cisco IOS XE Software, Version 17.03.04  "

stripped = version_raw.strip()
print("去掉空格: " + stripped)
print("转大写:   " + stripped.upper())
print("替换版本: " + stripped.replace("17.03.04", "17.06.01"))