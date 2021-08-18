#!/usr/bin/python3
"""A simple program to calculate water capture"""


def rain(walls):
    """
    rain: is a function that will calculate how
        many units of rain we can capture based on the
        height of walls in the list walls, and the space
        between each pair of walls.
    Parameters:
        walls - a list of non-neg ints that indicate
        either a wall (positive int) or a space (zero)
        any space between two walls is considered a
        capture zone which will be used to calculate
        our volume of potential water capture
    Return:
        a single int that accounts for total units
        of water that can be captured for this wall
        configuration.
    """
    totalVolume = 0

    for i in range(len(walls)):
        left_max = max(walls[:i + 1])
        right_max = max(walls[i:])
        totalVolume += max(min(left_max, right_max) - walls[i], 0)
    return totalVolume

if __name__ == '__main__':
    rain()
