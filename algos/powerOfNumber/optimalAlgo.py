"""
    Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to calculate using only logn 
    multiplications (instead of n multiplications required by the naive approach).

    It also has important applications in many tasks unrelated to arithmetic, since it can be used with any operations that have the 
    property of associativity:

    (X⋅Y)⋅Z=X⋅(Y⋅Z)
    (X+Y)+Z = X+(Y+Z)

    Most obviously this applies to modular multiplication, to multiplication of matrices and to other problems which we will discuss below.

    Information about the algorithm can be found here - https://cp-algorithms.com/algebra/binary-exp.html
"""

# import time function from time module for calculating the total execution time
from time import time


def power(base=3, exponent=13) -> float:
    """
        Uses binary exponentiation and then returns the power of a number of float type
    """
    # result to store the power of the number
    result = 1.0

    # till the exponent becomes zero keep the loop running
    # this loop runs for logn times instead of n times
    while exponent > 0:

        # if the exponent bit is set then multiply the reult and base and then store it inside result
        if exponent & 1:
            result *= base

        # keep incrementing the base by multiplying it with itself
        base *= base

        # right shift the exponent by one bit
        exponent >>= 1

    # final result is returned
    return result


# if this file is executed and not imported
if __name__ == "__main__":

    # note the start of the program
    start = time()
    result = power(base=2, exponent=23)
    print(f"{2}^({23}) = {result}")
    print("-------------------------------------------------------------------------------------------------------\n",
          "Total execution time:- ", time() - start, sep="")
