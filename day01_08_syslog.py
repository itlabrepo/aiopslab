import re

date = "2026-03-03"
hostname = "SW-Core-01"
level = "CRITICAL"
message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to up"

m = re.search(r"Interface (\S+), changed state to (\w+)", message)

if m:
    print(f"日期 : {date}")
    print(f"设备 : {hostname}")
    print(f"等级 : {level}")
    print(f"接口 : {m.group(1)}")
    print(f"状态 : {m.group(2)}")