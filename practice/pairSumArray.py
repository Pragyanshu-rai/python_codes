from timer import getExecTime


@getExecTime
def getTargetPairSumLinear(target: int = 31, array: list = [2, 4, 7, 11, 14, 16, 20, 21]) -> bool:
    """
        returns True if the sum of two elements in the array is equal to the target else returns False |
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    complements = dict()
    index = 0

    for index in range(len(array)):
        complements[array[index]] = index

    for index in range(len(array)):
        complement = complements.get(target-array[index], None)

        if complement is not None:
            return True

    return False


@getExecTime
def getTargetPairSum(target: int = 31, array: list = [2, 4, 7, 11, 14, 16, 20, 21]) -> bool:
    """
        returns True if the sum of two elements in the array is equal to the target else returns False | |
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
    """

    array.sort()
    start = 0
    end = len(array)-1

    while start < end:

        if array[start]+array[end] == target:
            return True

        if array[start]+array[end] > target:
            end -= 1

        else:
            start += 1

    return False


if __name__ == "__main__":
    print(getTargetPairSum())
    print(getTargetPairSum(-2, [4, -4, 6, -6, 10, -11, 12]))
    print(getTargetPairSum(21, []))
    print(getTargetPairSumLinear())
    print(getTargetPairSumLinear(-2, [4, -4, 6, -6, 10, -11, 12]))
    print(getTargetPairSumLinear(21, []))
