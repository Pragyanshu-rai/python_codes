def getMinDifference(array: list = [1, 4, 3, 2]) -> int:
    """
        Given the array of integers it returns the min difference between two of its equal subsets.
    """
    array = sorted(array)
    sum1 = sum2 = extra = 0
    size = len(array)

    if size % 2 != 0:
        extra = array[size//2]

    for index in range(size//2):
        currSum = array[index] + array[size - 1 - index]
        print(currSum, end=" ")

        if index % 2 == 0:
            sum1 += currSum
        
        else:
            sum2 += currSum

    if sum1 < sum2:
        sum1 += extra
    
    else:
        sum2 += extra

    return abs(sum1-sum2)


if __name__ == "__main__":

    print(getMinDifference())
    print(getMinDifference([1, 8, 9, 14]))
    print(getMinDifference([1, 3, 4, 6, 2, 5]))