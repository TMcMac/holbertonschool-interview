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
    row = 0
    perimeter = 0
    for row in range(len(grid)):
        col = 0
        for col in range(len(row)):
            if grid[row, col] == 0:
                continue
            else:
                if row == 0:
                    perimeter += 1
                elif row == (len(grid) - 1):
                    perimeter += 1
                if col == 0:
                    perimeter += 1
                elif col == (len(row) - 1):
                    perimeter += 1
                if grid[row, (col - 1)] == 0:
                    perimeter += 1
                if grid[row, (col + 1)] == 0:
                    perimeter += 1
    return perimeter
