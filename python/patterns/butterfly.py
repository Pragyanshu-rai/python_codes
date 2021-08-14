def printButterfly(size: int = 4) -> None:
    """
        Prints butterfly pattern of dimension size*2 by size*2 takes only one keyword argument "size" 
    """
    row = 1
    direction = 1
    change = False
    while row > 0:

        for col in range(1, size*2+1):

            if col <= row or col > ((2*size)-row):
                print("*", end="")

            else:
                print(" ", end="")

        print()
        if row == size and not change:
            change = True
            row += 1
            direction *= -1

        row += direction


# run this part if this file is executed directly
if __name__ == "__main__":
    printButterfly(7)
