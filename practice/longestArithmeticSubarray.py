from timer import getExecTime

@getExecTime
def longestArithmeticSubarray(array: list = [10, 7, 4, 6, 8, 10, 11]) -> int:
    """
        given an array of numbers this function returns the length of the longest arithmetic subarray
    """
    maxSofar = -1
    lastDifference = None
    currentLength = 1

    for index in range(1, len(array)):
        
        if array[index-1] - array[index] == lastDifference or lastDifference is None:
            lastDifference = array[index-1] - array[index]
            currentLength += 1
        
        elif array[index-1] - array[index] != lastDifference:
            lastDifference = array[index-1] - array[index]
            
            if currentLength > maxSofar:
                maxSofar = currentLength
            
            currentLength = 2

    return maxSofar


if __name__ == "__main__":
    print(longestArithmeticSubarray())