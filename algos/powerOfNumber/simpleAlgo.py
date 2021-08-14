# import time function from time module for calculating the total execution time
from time import time


def power(base=3, exponent=13) -> float:
    """
        Returns the power of a number float
    """
    num = base

    for _ in range(exponent, 1, -1):
        num *= base

    return num


# if this file is executed and not imported
if __name__ == "__main__":

    # note the start of the program
    start = time()
    result = power(base=2, exponent=23)
    print(f"{2}^({23}) = {result}")
    print("-------------------------------------------------------------------------------------------------------\n",
          "Total execution time:- ", time() - start, sep="")
