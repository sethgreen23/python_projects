#!/usr/bin/env python3

import datetime
import pytz

dt = datetime.datetime.now()
#aware time zone
#dt = datetime.datetime.now(tz=pytz.timezone("Africa/Algiers"))
print(dt)

#change to string 
#str_time = dt.isoformat()
str_time = dt.strftime("%Y-%m-%dT%H:%M:%S.%f")
print(str_time)
print(type(str_time))
#from isoformat (which is str) back to datetime
#dt_current = datetime.datetime.fromisoformat(str_time)
dt_current = datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S.%f")

print(dt_current)
print(type(dt_current))

