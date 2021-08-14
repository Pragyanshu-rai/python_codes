def getMinSwaps(array : list = [0, 1, 1, 1, 0, 1, 0, 1]) -> int:
    """
        returns minimum number of swaps required to bring all the 1 together
    """

    oneCount = sum(array)
    minswaps = 0
    maxFreq = 0
    currentFreq = 0
    maxFreqIndex = 0
    currentFreqIndex = 0

    for index in range(len(array)):

        if array[index] == 1:
            currentFreq += 1
            currentFreqIndex = index
        
        else:

            if currentFreq > maxFreq:
                maxFreq = currentFreq
                maxFreqIndex = currentFreqIndex

            currentFreq = 0

    for index in range(maxFreqIndex, maxFreqIndex+(oneCount-maxFreq)):

        if array[index] == 0:
            minswaps += 1


    return minswaps


print(getMinSwaps(), "\n----------")
print(getMinSwaps([0, 1, 0, 1, 1, 1, 0, 1, 1, 0]), "\n----------")
print(getMinSwaps([1,0,0,1,0,1]))
# getMinSwaps()