#!/usr/bin/env python3
import datetime
import pytz


# for timezone use this
# current utc time and time aware
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

#grab local time (naive time zone) with now
dt_local_datetime = datetime.datetime.now()
#use localize time function to change naive to aware
dt_tn = pytz.timezone('Africa/Algiers')
dt_local_datetime = dt_tn.localize(dt_local_datetime)
print(dt_local_datetime)


