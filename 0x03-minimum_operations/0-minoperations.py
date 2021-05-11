#!/usr/bin/python3
""" A script to find min operation to reproduce a charstring"""


def minOperations(n):
    """
    The function will start with a single char H and be given an int n
    the goal is for the program to find the least number of copy alls
    and pastes to get 'H' * n.

    n - an integer

    Return - least number of copy all and paste functions to get n h's
    """

    listH = 'H'
    currCopy = listH
    pst = 0
    cpy = 1

    if len(listH) >= n or type(n) is not int:
        return 0
    else:
        while len(listH) < n:
            if (2 * len(listH)) <= (n / 2):
                listH += listH
                cpy += 1
                pst += 1
                currCopy = listH
            else:
                listH += currCopy
                pst += 1
        return cpy + pst
