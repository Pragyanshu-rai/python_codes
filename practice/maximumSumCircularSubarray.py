from Timers.timer import getExecTime


@getExecTime
def getMaxCircularSubarraySum(array: list = [-1, 4, -6, 7, 5, -4]) -> int:
    """
        returns the max sum of a subarray of the given 'circular' array
    """
    currentSum = 0
    turns = 0
    index = 0

    if len(array) < 1:
        return None

    maxSofar = array[0]

    while turns < (len(array)*2)-2:

        currentSum += array[index]
        
        if currentSum < 0:
            currentSum = 0
        
        elif maxSofar is None or currentSum > maxSofar:
            maxSofar = currentSum

        index += 1
        turns += 1

        if index >= len(array):
            index = 0
    
    return maxSofar


if __name__ == "__main__":

    print(getMaxCircularSubarraySum())
    print(getMaxCircularSubarraySum([4, -4, 6, -6, 10, -11, 12]))
    print(getMaxCircularSubarraySum([]))