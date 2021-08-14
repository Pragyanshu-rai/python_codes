from timer import getExecTime


@getExecTime
def printZigzag(length: int = 9) -> None:
    """
        prints a zigazg pattern of height 3 and length provided as argument 'By default it takes the length to 9'
    """

    for row in range(1, 4):

        col = 1
        while col <= 3-row:
            print(" ", end=" ")
            col += 1

        # print(col)

        if row & 1 == 1:
            distance = 4
        else:
            distance = 2
        # print(distance)

        while col <= length:
            print("*", end=" ")
            col += distance
            for space in range(1, distance):
                print(" ", end=" ")

        print()


if __name__ == "__main__":
    printZigzag()
