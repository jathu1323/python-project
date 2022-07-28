# where is datetime in datetime library
from datetime import datetime, timedelta


current_date = datetime.now()
print ('Today is:  '+str(current_date))

# sub the day, month, year,hour,minute,second,microsecond

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))
print('Hour: ' + str(current_date.hour))
print('Minute: ' + str(current_date.minute))
print('Second: ' + str(current_date.second))
print('microsecond: ' + str(current_date.microsecond))

# timedelta using to define the time period of the time so
# use to backward or forward the time with the small code
# same procedure to change day, month, year,hour,minute,second,microsecond
one_day = timedelta(days=1) 
yesterday=current_date - one_day

print ('Yesterday this time was: ' + str(yesterday))


#store the str as datetime 

Birthday = input('When is your Birthday (dd/mm/yyyy)?  ')
Birthday_date = datetime.strptime(Birthday,'%d/%m/%Y')
print('Birthday: '+ str(Birthday_date))

