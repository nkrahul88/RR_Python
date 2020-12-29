#to get current date we need to import library from function
from datetime import datetime, timedelta

#this function returns a datetime objcet
current_date = datetime.now()
print('Today is : '+ str(current_date))

one_day = timedelta(weeks=1)
yesterday = current_date - one_day
print('Yesterday was :' + str(yesterday))

print('Day: '+ str(yesterday.day))
print('Month: ' + str(yesterday.month))
print('Year: '+ str(yesterday.year))

print('Hour: '+ str(yesterday.hour))
print('Minute: ' + str(yesterday.minute))
print('Second: '+ str(yesterday.second))