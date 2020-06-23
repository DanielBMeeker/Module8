"""
Program: set_membership.py
Author: Daniel Meeker
Date: 6/23/2020

This program defines a function - in_set() to find out
if a value is in a set or not.
"""


def in_set(a_set, value):
    """
    This function takes in a set and a value to determine
    if the value is in the set.

    :param a_set: A set to be searched
    :param value: The value being searched for in the set
    :return: Boolean True or False
    """
    if value in a_set:
        return True
    else:
        return False
