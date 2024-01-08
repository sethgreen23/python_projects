#!/usr/bin/env python3
import datetime
import pytz

# time zone aware
dt = datetime.datetime(2023, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

# for timezone use this
# current utc time and time aware
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

#doesnt have the option to add utc 
#but we can use the replace
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_now)
