#!/usr/bin/env python3

def canUnlockAll(boxes)
    """
    This program takes in a list of lists known as boxes
    each position in the list boxes is a box, and each box
    may contain one of more keys. The goal of the program is
    to check if based on the keys we have are we able to unlock
    all boxes. The box in position 0 of the list boxes will
    always be unlocked. Once we open the 0th box we will need
    to unlock all boxes that the 0th boxes contains keys for
    and contnue on collecting keys and unlocking boxes until
    we have unlocked all boxes or do not have keys to continue.
    If we unlock all we return True, else return False
    """

    n = len(boxes)
    unlocked = [0]
    lowestLocked = 1
    if n is not 0:
        keys = boxes[0]
    else:
        return True

    i = lowestLocked
    for(i in range(n)):
        if i in keys:
            keys.append(boxes[i])
