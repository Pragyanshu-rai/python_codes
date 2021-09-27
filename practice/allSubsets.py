from Timers.timer import getExecTime
from Prints.printUtil import print2D
from Bits.bitUtil import BitArray


def mapArray(target: list, mask: list) -> list:
    """
        Given a target array and a mask array this function returns the array after applying the mask. | 
        NOTE :- The size of target array and the mask array must be the same.
    """

    if len(target) != len(mask):
        return []

    result = list()

    for index in range(len(target)):

        if mask[index] == 1:
            result.append(target[index])

    return result


@getExecTime
def generateSubsets(array: list = [1, 3]) -> list:
    result = list()
    bitArray = BitArray(len(array))
    result.append(mapArray(array, bitArray.array))

    while bitArray.increment():        
        result.append(mapArray(array, bitArray.array))

    return result


if __name__ == "__main__":

    print2D(generateSubsets())
    print(generateSubsets())
    print2D(generateSubsets([5, 1, 6]))
    print(generateSubsets([5, 1, 6]))