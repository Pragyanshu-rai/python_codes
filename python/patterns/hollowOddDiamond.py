from timer import getExecTime


@getExecTime
def printOddDiamond(height: int = 4) -> None:
    """
        prints an odd diamond pattern of height = 2 * height provided
    """
    row = 1
    rowDirection = 1
    changeRowDirection = False

    while row > 0:

        col = 1
        while col <= height - row:
            print(" ", end=" ")
            col += 1

        for _ in range(1, 2*row):
            
            if _ == 1 or _ == (2*row)-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        if row == height and not changeRowDirection:
            row += 1
            rowDirection *= -1
            changeRowDirection = True
            # break

        print()
        row += rowDirection


if __name__ == "__main__":
    printOddDiamond()
