#!/usr/bin/env python3
import datetime
#naive datetime: easy to work with
#aware datetime: complicated but very aware

# pass normale integer without leading numbers
d = datetime.date(2016, 7, 24)
print(d)
# weekday(), year()
# iso weekdaty 1->7
# weekday 0->6
tday = datetime.date.today()
print(tday.day)

#time delta: difference between times
# deltat 7 days
tdelta = datetime.timedelta(days=7)
print(tday + tdelta) # day after 7 days

#date2 = date1 + timedelta
#  timedelta= date1 + date2

bday = datetime.date(2024, 5, 13)
till_bday = bday -  tday
print(till_bday)
# get just the days
print(till_bday.days)
# get it in seconds
print(till_bday.total_seconds())
