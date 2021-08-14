from timer import getExecTime


@getExecTime
def getSubarraySum(target: int = 5, array: list = [1, 2, 3, 8]) -> int:
    """
        given an array of integers and a target value this function will return the starting and ending index both inclusive of subarray (only positive numbers)
    """

    start = 0
    end = 0
    currentSum = 0

    if target == 0:

        if 0 in array:
            return array.index(0), array.index(0)

    while end < len(array):

        if currentSum == target and target != 0:
            return start, end-1

        if currentSum + array[end] <= target:
            currentSum += array[end]
            end += 1

        else:
            currentSum -= array[start]
            start += 1

        # print(start, end)

    return -1, -1


if __name__ == "__main__":

    print(getSubarraySum())
    print(getSubarraySum(33, [1, 4, 20, 3, 10, 5]))
    print(getSubarraySum(7, [1, 4, 0, 0, 3, 10, 5]))
    print(getSubarraySum(0, [-1, 4]))
