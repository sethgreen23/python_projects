#!/usr/bin/env python3

import datetime

#hour minute second microscond naive
t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)
# year month and aday
d = datetime.date(2015, 5, 13)
print(d)

dt = datetime.datetime(2015, 5, 13, 8, 3, 54, 100000)
print("dt: ",dt)
# it works with hours and others
tdelta = datetime.timedelta(days=7)
print("dt + tdelta: ",dt + tdelta)
print(dt.date())
print(dt.time())
print(dt.year)

