import datetime
import time
import calendar

tod = datetime.datetime.today()
days5 = datetime.timedelta(days=5)

print(tod)
print(tod.year)
print(tod.month)
print(tod.weekday())

print(tod - days5)
print(tod + days5)