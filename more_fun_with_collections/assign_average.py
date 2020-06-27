"""
Program: assign_average.py
Author: Daniel Meeker
Date: 6/27/2020

This program defines a switch_average function that emulates
the case statement of other languages using a dictionary.
"""


def switch_average(key):
    """
    This function takes in a dictionary and performs a
    switch selection on the dictionary using a key. If the
    key is not in the dictionary it will raise a ValueError.
    This function allows for a slight typo from where it is
    called by always capitalizing the key before using it.

    :param key: a key used to search the dictionary
    :return: the value of the key
    """
    a_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
    if str(key).capitalize() == 'A':
        return a_dict.get(str(key).capitalize())
    elif str(key).capitalize() == 'B':
        return a_dict.get(str(key).capitalize())
    elif str(key).capitalize() == 'C':
        return a_dict.get(str(key).capitalize())
    elif str(key).capitalize() == 'D':
        return a_dict.get(str(key).capitalize())
    elif str(key).capitalize() == 'F':
        return a_dict.get(str(key).capitalize())
    else:
        raise ValueError()


if __name__ == '__main__':
    pass
