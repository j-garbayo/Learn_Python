#DATETIME

'''
Python has the datetime module to help deal with timestamps in your code. Time values are represented with the time class. TImes
have atributes for hour, minute, second and microsecond. They can also include time zone information. The arguments to initialize
a time instance are optional, but the default of 0 is unlikely to be what you want
'''

#datetime.time
#Lets you create a timestamp

from datetime import time

t = time(4, 20, 1)

print t
print 'hour  :', t.hour
print 'minute:', t.minute
print 'second:', t.second
print 'microsecond:', t.microsecond
print 'tzinfo:', t.tzinfo

#Note: a time instance only holds values of time, and not a date associated with the time.

#We can also check the min and max values a time of a day can have in the module
#The min and max class attributes reflect the valid range of times in a single day.

print 'Earliest  :', time.min
print 'Latest    :', time.max
print 'Resolution:', time.resolution

#Dates
#datetime (as you might suspect) also allows us to work with date timestamps. Calendar date values are represented with
#the date class. Instances have attributes for year, month and day. It is easy to create a date representing today's date
#using the today() class method.

from datetime import date

today = date.today()

print today
print 'ctime:', today.ctime()
print 'tuple:', today.timetuple()
print 'ordinal:', today.toordinal()
print 'Year:', today.year
print 'Mon :', today.month
print 'Day :', today.day

#the range of date values supported can be determined using the min and max attributes

print 'Earliest  :', date.min
print 'Latest    :', date.max
print 'Resolution:', date.resolution

#Another way to create new date instances used the replace() method of an existing date. 
#For example, you can change the year, leaving the day and month alone.

d1 = date(2015,3,11)
print 'd1:', d1

d2 = d1.replace(year=1990)
print 'd2:', d2

#Arithmetic of date objects to check for time differences:

difference = d1-d2
print(difference)
print(difference.days)

from datetime import timedelta

