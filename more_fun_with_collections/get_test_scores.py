"""
Program: get_test_scores.py
Author: Daniel Meeker
Date: 6/25/2020

This program defines two functions, one to get input for a dictionary
and another to average the input of the dictionary.
"""


def get_test_scores():
    """
    This function prompts the user for the number of tests to be entered
    and the test scores for each test. It validates the input and if valid
    will add the scores to a dictionary.
    :return: a dictionary of scores
    """
    scores_dict = dict()
    num_scores = input("How many test scores would you like to enter? ")
    if not num_scores.isnumeric():
        raise ValueError("Please enter a positive integer for number of test scores.")
    else:
        for x in range(0, int(num_scores)):
            score = input("Please enter a test score: ")
            if not str(score).isnumeric():
                raise ValueError("Scores must be a positive integer")
            elif float(score) < 0:
                raise ValueError("Scores can't be negative")
            elif float(score) > 100:
                raise ValueError("Scores can't be higher than 100")
            else:
                scores_dict["Test " + str(x+1)] = score
    return scores_dict


def average_scores(a_dict):
    """
    This function takes in a dictionary and averages the values in
    the dictionary
    :param a_dict: the dictionary passed in
    :return: the average of the values in the dictionary
    """
    num_scores = len(a_dict)
    total = 0
    for key, value in a_dict.items():
        total += int(value)
    return total / num_scores


if __name__ == '__main__':
    try:
        print(average_scores(get_test_scores()))
    except ValueError as e:
        print(e)
