def leap_years(year: int) -> bool:
    """
    Take a single integer parameter representing a year (e.g. 2018),
    and return: True if the year is a leap year, and False if not.
    As a reminder, a leap year occurs when the year is a multiple of four,
    unless the year is a multiple of 100.
    However, if the year is a multiple of 400, then it is a leap year.
    For instance, 2016 and 2000 are leap years, but 2100 is not.
    Args:
        year (int): Input a year.

    Returns:
        bool: Whether this year is a leap year or not.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
