#!/usr/bin/env python3
import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.timezone('Africa/Algiers'))
print(dt_utcnow)
#display date times
#using iso format
print(dt_utcnow.isoformat())
# formating the dates
print(dt_utcnow.strftime('%B %d, %Y'))
# str to datetime
dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to string
# strptime - string to Datetime

# arrow module for datetime
