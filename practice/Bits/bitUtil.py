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


class BitArray:
    """
        Data Structure used to create a bit array.
    """

    array = None
    size = None

    def __init__(self, size: int = 64) -> None:
        self.array = [0] * size
        self.size = size
    
    def increment(self, step: int = 1) -> bool:
        """
            takes step as an argument to increment the bit array, if no step is provided it will increment the array by 1 |
            returns True if the array is incremented without any error and False if the array overflows due to the increment.
        """
        # print(self.array)

        try:

            while step > 0:
                index = self.size - 1
                bit = 1

                # print(index, bit)
            
                while index >= -1:

                    # print(index, bit, self.array)
                    if bit == 0:
                        break
                    
                    else:

                        if self.array[index] == 0:
                            self.array[index] = bit
                            bit = 0
                        
                        else:
                            self.array[index] = 0
                    
                    index -= 1
                
                else:
                    return False

                step -= 1
            
            return True

        except:

            return False
    
    def __repr__(self) -> str:
        
        return "array - "+str(self.array)+", size - "+str(self.size)


if __name__ == "__main__":
    print(setBit(4, 1))
    print(checkBit(2, 1))
    print(checkBit(2, 1, 0))

    bitArray = BitArray(4)
    
    for num in range(15):
        
        print(bitArray.array)
        print(bitArray.increment())
    
    print(bitArray.array)


    bitArray = BitArray(5)

    print(bitArray.array)
    print(bitArray.increment(23))
    print(bitArray.array)
    print(bitArray.increment(23))
    print(bitArray.array)