import datetime, time, calendar

birthday = datetime.date(1986,5,5)
next_birthday = datetime.date(2020,5,5)
tod = datetime.date.today()
dif = next_birthday - tod

d = datetime.timedelta(days = 1)
yest = tod - d
yest_add2 = yest + d*2
yest_sub3 = yest - d*3

print(birthday)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.isoweekday())
print(dif)
print("\n")
print(calendar.month(2017,5))

print(yest, yest_add2, yest_sub3)
