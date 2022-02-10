# import time function from time module for calculating the total execution time
from time import time


def getRunTime(function):
    """
        function decorator to calculate the runtime of a python function
        use '@getRunTime'
    """

    def mainWrapper(*args, **kwargs):
        """
            wrapper function used calculate the runtime and call the function passed 
        """

        # get the start time
        start = time()

        # call the function
        print(function(*args, **kwargs))

        # print the total runtime of the function
        print("-------------------------------------------------------------------------------------------------------\n",
              "Total execution time:- ", time() - start, sep="")

    # return the reference to the inner wrapper function
    return mainWrapper
