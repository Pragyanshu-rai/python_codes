#bitUtil module


def setBit(number: int, position: int, bit: int = 1) -> int:
    """
        returns the number with its 'bit' set at the at the given 'position'  
    """

    return number | 1 << position


def checkBit(number: int, position: int, bit: int = 1) -> bool:
    """
        returns True if the specific 'bit' is set in the specific position in the number
    """

    if number & 1 << position == bit << position:
        return True

    return False


if __name__ == "__main__":
    print(setBit(4, 1))
    print(checkBit(2, 1))
    print(checkBit(2, 1, 0))