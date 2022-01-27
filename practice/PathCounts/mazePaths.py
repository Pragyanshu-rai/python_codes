def countAllPaths(size: int, right: int, down: int) -> int:
    """
        returns the count of all the possible paths from the start to the end of the maze of dimension size x size.
    """

    if right == size-1 and down == size-1:
        return 1
    
    if right > size-1 or down > size-1:
        return 0
    
    return countAllPaths(size, right+1, down) + countAllPaths(size, right, down+1)


if __name__ == "__main__":

    print(countAllPaths(2, 0, 0))