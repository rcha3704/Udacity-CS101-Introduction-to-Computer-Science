# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
from datetime import date

# Number of days in each month
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Checks if the given year is a leap year
def isLeapYear(year):
    if (year%4 != 0):
        return False
    elif (year%100 != 0):
        return True
    elif (year%400 != 0):
        return False
    else:
        return True

# Returns the days in the given years          
def days_in_years(year1, year2, month1, month2, day1, day2):
    y1 = year1
    yrs = year2-year1
    
    # To cater for dates where month1 > month2 
    if (month1>month2):
        yrs-=1
    
    days = yrs*365
    
    if(isLeapYear(year1)):
        if (month1<=2 and month2>2):
            days+=1
        elif (month2==2 and day2>28):
            days+=1
    
    year1+=1
    
    while(year1<year2):
        if (isLeapYear(year1)):
            days+=1
        year1+=1

    if(y1!=year2 and isLeapYear(year2)):
        if (month2>2 or (month2==2 and day2>28)):
            days+=1
            
    
    # days = 0
    # y1 = year1
    
    # while (y1<year2):
    #     days += 365
    #     if (isLeapYear(y1)):
    #         days += 1
    #     y1 += 1
    
    # # If the last year is a leap year and the month is past February, add an extra day
    # if (month2>2 and isLeapYear(year2)):
    #     days+=1
            
    return days
    
# Returns the number of days in between the given months    
def days_in_months(month1, month2):
    days = 0
    if (month1 <= month2):
        while (month1 < month2):
            days += daysOfMonths[month1-1]
            month1 += 1
    else:
        while (month1 <= 12):
            days += daysOfMonths[month1-1]
            month1+=1
        
        month1 = 1
        
        while (month1 < month2):
            days += daysOfMonths[month1-1]
            month1+=1
        
    return days

# Returns the number of days 
def days(day1, day2):
    return day2-day1

# Returns number of days utilizing datetime. Easier and less error prone.      
def number_of_days(year1, month1, day1, year2, month2, day2):
    d1 = date(year1,month1,day1)
    d2 = date(year2,month2,day2)
    
    diff = d2-d1
    ndays = diff.days
    
    return ndays

# Returns the number of days in between two given dates
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    total_days = 0
    
    total_days = days_in_years(year1, year2, month1, month2, day1, day2)
    total_days += days_in_months(month1, month2)
    total_days += days(day1,day2)
    
    # total_days = number_of_days(year1, month1, day1, year2, month2, day2)
    # print total_days
    return total_days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((2011,10,1,2012,3,1), 152),
                  ((2011,3,1,2012,1,1), 306)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed ", result
        else:
            print "Test case passed!"

test()
