from Timers.timer import getExecTime


def getSmallestPrimeFactor(limit: int = 50) -> dict:
    """
        returns a dict of numbers and its smallest prime factor as a key and value pair respectively
    """

    smallestPrimeFactors = {number: -1 for number in range(1, limit+1)}
    number = 1

    while number*number < limit:
        number += 1

        if number != 2 and number % 2 == 0:
            continue

        if smallestPrimeFactors[number] == -1:
            smallestPrimeFactors[number] = number

            for num in range(number*number, limit+1, number):
                smallestPrimeFactors[num] = number
    
    # spf => smallest prime factor
    for number, spf in smallestPrimeFactors.items():

        if spf == -1:
            smallestPrimeFactors[number] = number

    return smallestPrimeFactors


@getExecTime
def getPrimeFactors(target: int = 31) -> list:
    """
        returns a list of prime factors of the target number
    """

    SPF = getSmallestPrimeFactor(target)
    primeFactors = list()

    while target > 1:
        spf = SPF.get(target)
        primeFactors.append(spf)
        target /= spf

    return primeFactors


if __name__ == "__main__":
    print(getPrimeFactors())
    print(getPrimeFactors(0))
    print(getPrimeFactors(20))
    print(getSmallestPrimeFactor())
