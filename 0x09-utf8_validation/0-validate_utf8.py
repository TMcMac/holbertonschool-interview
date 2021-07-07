#!/usr/bin/python3
"""A Simple function to check UTF8 chars"""


def validUTF8(data):
    """
    Function: validUTF8
    Description: Validates whether the integers in a list
    represent valid UTF-8 characters.
    Args: data: list of ints
    Return:True if valid UTF8 chars or False if not
    """

    if len(data) == 0:
        return True
    if len(data) == 1:
        if data[0] >= 32 and data[0] <= 126:
            return True
        else:
            return False

    for num in data:
        if num > 31 and num < 127:
            continue
        elif num == 0:
            continue
        else:
            return False

    return True
