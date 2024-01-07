#!/usr/bin/env python3
import datetime
import pytz


# for timezone use this
# current utc time and time aware
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

#convert to my time
#print(pytz.all_timezones)
# Tunisian time zone
dt_tn = dt_utcnow.astimezone(pytz.timezone('Africa/Algiers'))
print(dt_tn)
#difference between utc time and tunisian time

