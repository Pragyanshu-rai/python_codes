"""
    This is the implementation of Sieve of Eratosthenes.

    Sieve of Eratosthenes is an algorithm for finding all the prime numbers in a segment [1;n] using O(nloglogn) operations.

    information aout this algorithm can be found here https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
"""


from runTime import getRunTime


@getRunTime
def primeRange(upper: int = 50) -> list:
    """
        Returns the list of prime numbers in the range [0, upper) and takes int as argument
    """

    # This will create a dictionary with numbers in range [lower, upper) and if the number is > 1 and odd except 2 and map it with True
    numbers = {num: True for num in range(
        upper) if num > 1 and (num == 2 or num & 1 == 1)}
    # Main Algorithm
    num = 2
    
    while (num*num) < upper:

        if num & 1 == 0:
            num += 1
            continue

        if numbers[num]:

            # starting from square of the number to upper limit with sept as the number itself
            for multiples in range(num*num, upper, num):
                numbers[multiples] = False

        num += 1

    # print(numbers)
    # This will create a list with all keys which are true in numbers dictionary
    return [key for key in numbers.keys() if numbers[key] == True]


if __name__ == "__main__":

    primeRange(999999)
