# Days in Month
# convert this function is_leap(), so that instead of printing "Leap year." or "Not leap year." it
# should return True if it is a leap year and return False if it is not a leap year.

# create a function called days_in_month() which will take a year and a month as inputs


def is_leap(year):
    """ The function takes a year and returns True if it is a leap year or False if it is not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month entered."
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
