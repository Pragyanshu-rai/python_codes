# import time function from time module for calculating the total execution time
from time import time

from math import sqrt


def isPrime(number: int) -> bool:
    """
        Returns true if number is a prime number and false if it is not
    """
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0:
        return False

    last = int(sqrt(number)) + 1

    for num in range(3, last + 1, 2):
        if number % num == 0:
            return False

    return True


def primeRange(upper: int = 50) -> list:
    """
        Returns the list of prime numbers in the range [0, upper) and takes int as argument
    """

    primes = list()

    for number in range(upper):
        if isPrime(number):
            primes.append(number)

    return primes


if __name__ == "__main__":

    # note the start of the program
    start = time()

    # this will print the list of prime less than 999999
    print(primeRange(999999))
    print("-------------------------------------------------------------------------------------------------------\n",
          "Total execution time:- ", time() - start, sep="")
