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

    hs = ['H']  # Our starting text file contains 1 * 'H'
    currCopy = ['H']  # Anything greater than n=1 will require a copy operation
    operations = 0  # Count of number of operations

    if n <= 1 or isinstance(n, int) is False:
        return 0
    elif n > 536870912:
        hs = 1
        currCopy = 1
        while hs < n:
            if (n % (hs * 2) == 0) or (n % hs == 0):
                currCopy = hs
                hs * 2
                operations += 2
            else:
                hs += currCopy
                operations += 1
    else:
        while len(hs) < n:
            double = (2 * len(hs))
            if (n % double == 0):
                currCopy = list(hs)  # Copy all doubling th goes into n
                hs.extend(hs)  # This is a paste all
                operations += 2  # That means two operations
            elif (n % len(hs) == 0):
                currCopy = list(hs)  # Copy all as current list goes into n
                hs.extend(hs)  # This is a paste all
                operations += 2  # That means two operations
            else:
                hs.extend(currCopy)
                operations += 1  # This is one paste function
    return operations
