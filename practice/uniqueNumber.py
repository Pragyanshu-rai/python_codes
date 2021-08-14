from timer import getExecTime
from bitUtil import setBit, checkBit


@getExecTime
def getUniqueNumber(array: list = [4, 2, 6, 3, 4, 6, 2]) -> int:
    """
        returns the unique number present in a list
    """

    xorSum = 0

    for element in array:
        xorSum ^= element
    
    return xorSum


@getExecTime
def getTwoUniqueNumbers(array: list = [4, 2, 6, 5, 7, 2, 4, 6]) -> tuple:
    """
        returns a tuple of two unique numbers in a list
    """

    xorSum = 0
    position = 0
    currentBit = 0
    newXORSum = 0 

    for element in array:
        xorSum ^= element
    
    while currentBit == 0:
        position += 1
        currentBit = xorSum & 1 << position
    
    for element in array:
        
        if checkBit(element, position):
            newXORSum ^= element
    
    return (newXORSum, xorSum ^ newXORSum)



@getExecTime
def getUniqueFromThree(array: list = [1, 3, 2, 3, 4, 2, 1, 1, 3, 2]) -> int:
    """
        returns the unique number from in the list
    """

    result = ['0']*len(bin(max(array))[2:])

    for position in range(len(result)):
        bits = 0
        
        for number in array:

            if checkBit(number, position):
                bits += 1
            
        # if bits % 3 != 0:
        #     result.append(1)
        result[position] = str(bits % 3)

    return int("".join(result[::-1]), base=2)


if __name__ == "__main__":
    print(getUniqueNumber())
    print(getTwoUniqueNumbers())
    print(getUniqueFromThree())