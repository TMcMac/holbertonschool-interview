#!/usr/bin/python3

def island_perimeter(grid):
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
