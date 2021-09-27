# printUtil Module

def print2D(grid: list = [[0],[0]]) -> None:
    """
        Given a 2d array as an argument this function prints the 2d array in matrix or grid representation. | 
        if called without and argument this funtion prints a 1 X 2 matrix or grid.
    """

    for row in grid:

        for element in row:

            print(element, end = " ")

        print()