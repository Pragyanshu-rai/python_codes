from Timers.timer import getExecTime


@getExecTime
def smallestMissingPositveNumber(array: list = [0, -9, 1, 3, -4, 5]) -> int:
    """
        provided an array of elements this function returns the smallest missing positive number  
    """

    checkList = [False]*len(array)

    for element in array:
        
        if len(array) > element >= 0:
            checkList[element] = True

    try:
        return checkList.index(False)
    except:
        return len(checkList)


if __name__ == "__main__":
    print(smallestMissingPositveNumber())