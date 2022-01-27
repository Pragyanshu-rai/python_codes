from Timers.timer import getExecTime


@getExecTime
def getMaxSubarraySum(array: list = [1, -2, 4, -6, 7, 2]) -> int:
    """
        returns the max sum of a subarray of the given array
    """
    currentSum = 0
    maxSofar = None

    for element in array:

        currentSum += element

        if currentSum < 0 :
            currentSum = 0

        elif maxSofar is None or currentSum > maxSofar:
            maxSofar = currentSum
        
    return maxSofar

if __name__ == "__main__":

    print(getMaxSubarraySum())
    print(getMaxSubarraySum([-2, -3, 4, -1, -2, 1, 5, -3]))
    print(getMaxSubarraySum([]))