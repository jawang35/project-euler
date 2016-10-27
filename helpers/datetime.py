import datetime

def day_of_week(date):
    jan_1_1900 = 1
    days_from_jan_1_1900 = (date - datetime.date(1900, 1, 1)).days
    return (jan_1_1900 + days_from_jan_1_1900) % 7
