"""
Program: half_birthday.py
Author: Daniel Meeker
Date: 6/28/2020

This program defines a half birthday function that calculates
the half birthday of a given birthday.
"""
import datetime
from datetime import timedelta


def half_birthday(birthday_datetime):
    """
    This function calculates your half-birthday using timedelta
    with the weeks argument.
    :param birthday_datetime: a datetime representing birthday
    :return: the datetime of the half birthday
    """
    half_b_day = (datetime.date(birthday_datetime.year,
                                birthday_datetime.month,
                                birthday_datetime.day)
                  + datetime.timedelta(weeks=26))
    return half_b_day.isoformat()
