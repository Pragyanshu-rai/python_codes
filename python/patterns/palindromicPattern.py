def palindromicPattern(height: int = 5) -> None:
    """
        prints a palindromic pattern or numbers from 1 to height of height 'height'
    """

    row = 1
    while row <= height:

        col = 1
        # print(height-row)
        while col <= height-row:
            print(" ", end=" ")
            col += 1

        col = row
        move = -1
        for count in range(1, row*2):

            print(col, end=" ")

            if col == 1:
                move *= -1

            col += move

        print()
        row += 1


if __name__ == "__main__":
    palindromicPattern()
