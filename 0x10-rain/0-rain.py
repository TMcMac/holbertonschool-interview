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
    i = 0
    rightWall = 0
    leftWall = 0
    totalVolume = 0
    rwPos = 0
    lwPos = 0

    while i < len(walls):
        if walls[i] != 0 or i + 1 == len(walls):
            totalVolume += ((rwPos - lwPos) * min(leftWall, rightWall))
            leftWall = rightWall
            lwPos = rwPos
            rightWall = walls[i]
            rwPos = i
        i += 1
    return totalVolume

if __name__ == '__main__':
    rain()
