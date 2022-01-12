#!/usr/bin/python3
""" Pascals Triangle """


def pascal_triangle(n):
    """
        This function is designed to return a
        pascals triangle of n height.
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        triangle.append([1])
        row = 1
        while row < n:
            newRow = []
            mover = 0
            prevRowLen = len(triangle[(row - 1)])
            while mover <= prevRowLen:
                if mover == 0:
                    newRow.append(1)
                elif mover == prevRowLen:
                    newRow.append(1)
                else:
                    newRow.append((triangle[(row - 1)][(mover - 1)] +
                                   triangle[(row - 1)][mover]))
                mover += 1
            triangle.append(newRow)
            row += 1
        return triangle
