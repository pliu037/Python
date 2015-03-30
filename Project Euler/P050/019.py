#https://projecteuler.net/problem=19

'''
Finds and returns the number of Sundays that fall on the first of a month between Jan 1 of year x and
Dec 31 of year y given that Jan 1, 1900 is a Monday
Method:
Starting with day = 0 (Monday) on Jan 1, 1900, loop through each month, adding the number of days in
that month, adjusted for leap years. An invariant is that day always represents the first day of a
month. Day modulo the number of days in a week, then, yields the day of the week (6 is Sunday).
'''
def countSundays(x, y):
    #The number of days in each month (with index 0 being January)
    DAYSINMONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    LEAPYR_FEBDAYS = 29
    LEAPYR_INTERVAL = 4
    DAYSINWEEK = 7
    
    day = 0
    year = 1900
    sundays = 0
    while year <= y:
        for month in xrange(len(DAYSINMONTH)):
            
            '''
            If the first day of the month is Sunday and the year is greater than or equal to x, add 1
            to sundays
            '''
            if (day == 6 and year >= x):
                sundays += 1
            
            days = DAYSINMONTH[month]
            
            '''
            It is a leap year (year is divisible by LEAPYR_INTERVAL, but not by 100, unless also
            divisible by 400)
            '''
            if (((year % LEAPYR_INTERVAL == 0) and (year % 100 != 0)) or (year % 400 == 0)):
                
                #It is February: days is set to LEAPYR_FEBDAYS
                if month == 1:
                    days = LEAPYR_FEBDAYS
                    
            #Given the number of days in this month, determine the first day of the next month
            day += days
            day = day % DAYSINWEEK
            
        year += 1
    return sundays
    
print countSundays (1901, 2000)