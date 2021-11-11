#!/usr/bin/python3
"""
A interview question for finding the perimeter of
islands in a matrix
"""


def island_perimeter(grid):
    """
        We are given a matrix of 1s and 0s where 1s are land
        and zeros are water, we need to find the length of the
        perimeter of all the islands on our grid.
    """
    row = -1
    perimeter = 0
    for fullrow in grid:
        col = 0
        row += 1
        for col in range(len(fullrow)):
            if grid[row][col] == 0:
                # if we have a 0 we are at sea
                continue
            else:
                # if we have a 1 at this location we are on land
                if row == 0:
                    # if we are in the first row, on land, the top is a border
                    perimeter += 1
                elif grid[(row - 1)][col] == 0:
                    # if not the top row, but previous [row, this col] is water
                    perimeter += 1
                if row == (len(grid) - 1):
                    # if we are in the last row, on land, the bottom is border
                    perimeter += 1
                elif grid[(row + 1)][col] == 0:
                    # if not the bottom, but next [row,this col] is water
                    perimeter += 1
                if col == 0:
                    # if on the left edge of the grid
                    perimeter += 1
                elif grid[row][(col - 1)] == 0:
                    # if not the left edge but previous space is water
                    perimeter += 1
                if col == (len(fullrow) - 1):
                    # if on the right edge of the grid
                    perimeter += 1
                elif grid[row][(col + 1)] == 0:
                    # if not the right edge but the next space is water
                    perimeter += 1
    return perimeter
