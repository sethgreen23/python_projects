#!/usr/bin/env python3

import datetime

#current time with localzone of none naive
dt_today = datetime.datetime.today()
# option to add timezone naive
dt_now = datetime.datetime.now()
# give utc time with tz infor to none naive
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
