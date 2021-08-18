#!/usr/bin/python3
"""A simple program to calculate water capture"""
from typing import List


def rain(walls: List[int]) -> int:
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
    rwPosition = 0
    lwPosition = 0

    while i < len(walls):
        if walls[i] != 0:
            totalVolume += ((rwPosition - lwPosition) * min(leftWall, rightWall))
            leftWall = rightWall
            lwPosition = rwPosition
            rightWall = walls[i]
            rwPosition = i
        i += 1
    return totalVolume

if __name__ == '__main__':
    rain()
