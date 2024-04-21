import datetime
curr = datetime.datetime.now()
#print(curr)

year = curr.year
month = curr.month
day = curr.day
date = curr.date()

#print(year,month,day, date)

new_date = curr + datetime.timedelta(days=35)
print(new_date)