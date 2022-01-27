from Timers.timer import getExecTime

@getExecTime
def matrixSearch(matrix: list, target: int = 5) -> bool:
    """
        returns true if the target element is found in the sorted matrix else it returns false 
    """

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    row = 0
    cell = len(matrix[0])-1

    while row < len(matrix) and cell >= 0:

        # return True if the target element is found
        if target == matrix[row][cell] :
            return True
        
        # go down a row if the target elemnt is greater
        if target > matrix[row][cell] :
            row += 1
        
        # slide to the cell which is left to the current cell
        else:
            cell -= 1

    return False


if __name__ == "__main__":
    matrix = list()
    element = 1
    
    for row in range(5):
        matrix.append(list())

        for col in range(5):
            matrix[row].append(element)
            element += 1

    print(matrixSearch(matrix=matrix))
    print(matrixSearch(matrix, 28))
    print(matrixSearch(matrix, 7))
