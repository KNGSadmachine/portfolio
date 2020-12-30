import sys
import datetime
import re

print(sys.version)

Start_time = str(datetime.datetime.now())
Start_time = re.split("[-:. ]", Start_time)
Start_time.pop(-1)
Start_time = map(str, Start_time)
Start_time_str = "".join(Start_time)
Start_time = int(Start_time_str)
print(Start_time)