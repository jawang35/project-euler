'''
Problem 19 - Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
- April, June and November.
- All the rest have thirty-one,
- Saving February alone,
- Which has twenty-eight, rain or shine.
- And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec
2000)?
'''

from functools import partial
from datetime import date
from helpers.runtime import print_answer_and_elapsed_time
from helpers.datetime import day_of_week

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def counting_sundays(start, end):
    sundays_on_first_of_month = 0
    current_day_of_week = day_of_week(start)
    for year in range(start.year, end.year + 1):
        leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 > 0)
        for month in range(1, 13):
            if current_day_of_week is None:
                current_day_of_week = day_of_week(start)
            elif leap_year and month == 2:
                current_day_of_week += (days_in_month[2] + 1)
            else:
                current_day_of_week += days_in_month[month]
            if current_day_of_week % 7 == 0:
                sundays_on_first_of_month += 1
    return sundays_on_first_of_month

if __name__ == '__main__':
    start = date(1901, 1, 1)
    end = date(2000, 12, 31)
    print_answer_and_elapsed_time(partial(counting_sundays, start, end))
