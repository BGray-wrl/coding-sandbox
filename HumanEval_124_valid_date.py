def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    if not date:
        return False

    parts = date.split('-')
    if len(parts) != 3:
        return False

    month_str, day_str, year_str = parts

    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False

    if not (len(month_str) == 2 and len(day_str) == 2 and len(year_str) == 4):
        return False

    month = int(month_str)
    day = int(day_str)
    year = int(year_str)

    if not (1 <= month <= 12):
        return False

    days_in_month = {
        1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
        4: 30, 6: 30, 9: 30, 11: 30,
        2: 29
    }

    if not (1 <= day <= days_in_month.get(month, 0)):
        return False

    return True