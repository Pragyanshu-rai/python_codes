# Premutations module

class NotAListError(BaseException):

    def __repr__(self):
        return "NotAListError"

def safePermutate(result : list, sequence, index) -> None:
    """
        Recursive function used to find all the possible permutation of the given sequence. |
        Time complexity - O(n!)  
        NOTE :- This function only returns the non duplicate permutation of the given sequence.
    """
    if type(sequence) != list:
        raise NotAListError()
    
    size = len(sequence)

    if(index == size):
        sequence = "".join(sequence)
        
        if sequence not in result:
            result.append(sequence)
        return None

    for ptr in range(index, size):

        if ptr != index and sequence[ptr] == sequence[index]:
            continue
        
        sequence[ptr], sequence[index] = sequence[index], sequence[ptr]
        safePermutate(result, sequence, index+1)
        sequence[ptr], sequence[index] = sequence[index], sequence[ptr]


def getSafePermutations(sequence) -> list:
    """
        Given the sequence this function returns a list of all its possible permutations. |
        NOTE :- This function only returns the non duplicate permutation of the given sequence.
    """
    result = list()

    safePermutate(result, sorted(sequence), 0)

    return result


def permutate(result : list, subSequence, sequence) -> None:
    """
        Recursive function used to find all the possible permutation of the given sequence. |
        Time complexity - O(n!)  
    """
    size = len(subSequence)
    index = 0 

    if size == 0:
        result.append(sequence)
        return None
    
    while index < size:

        permutate(result, subSequence[:index]+subSequence[index+1:], sequence+subSequence[index]) 
        index += 1


def getPermutations(sequence) -> list:
    """
        Given the sequence this function reutrns a list of all its possible permutations.
    """
    result = list()

    permutate(result, sequence, "")

    return result