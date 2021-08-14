from timer import getExecTime


def printSpiral(matrix: list) -> None:
    """
        prints the given matrix in spiral pattern
    """

    for row in matrix:

        for cell in row:
            print("{:02}".format(cell), end=" ")

        print()


@getExecTime
def spiralPattern(rowLimit: int = 5, columnLimit: int = 5) -> None:
    """
        stores number 1 to rowLimit * columnLimit in spiral order inside an rowLimit x columnLimit matrix
    """

    array = [[n for n in range(columnLimit)] for x in range(rowLimit)]
    columnStart = rowStart = 0
    rowEnd = rowLimit - 1
    columnEnd = columnLimit - 1
    num = 1

    while rowStart <= rowEnd and columnStart <= columnEnd:

        cell = rowStart

        while cell <= columnEnd:
            array[rowStart][cell] = num
            cell += 1
            num += 1

        rowStart += 1
        cell = rowStart

        while cell <= rowEnd:
            array[cell][columnEnd] = num
            cell += 1
            num += 1

        columnEnd -= 1
        cell = columnEnd

        while cell >= columnStart:
            array[rowEnd][cell] = num
            cell -= 1
            num += 1

        rowEnd -= 1
        cell = rowEnd

        while cell >= rowStart:
            array[cell][columnStart] = num
            cell -= 1
            num += 1

        columnStart += 1

    printSpiral(array)


if __name__ == "__main__":

    print(spiralPattern(5, 4))
    print(spiralPattern())
    print(spiralPattern(7))
