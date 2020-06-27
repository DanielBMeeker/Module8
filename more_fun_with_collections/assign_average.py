def switch_average(a_dict, key):
    """
    This function takes in a dictionary and performs a
    switch selection on the dictionary using a key. If the
    key is not in the dictionary it will raise a ValueError.
    This function allows for a slight typo from where it is
    called by always capitalizing the key before using it.

    :param a_dict: a dictionary to be searched
    :param key: a key used to sort the dictionary
    :return: the value of the key
    """
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
