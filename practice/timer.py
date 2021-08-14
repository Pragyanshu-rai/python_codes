from time import time


def getExecTime(functionToRun):
    """
        function decorator to calculate the runtime of a python function
        use '@getExecTime'
    """

    def innerFunction(*args, **kwargs):
        """
            innerfunction used to calculate the runtime and call the fuction passed as an argument
        """

        # get the start time
        start = time()
        result = None

        print(f"Started executing - {functionToRun.__name__}\n",
              "-------------------------------------------------------------------------------------------------------", sep="")

        # call the function
        result = functionToRun(*args, **kwargs)

        # print the total runtime of the function
        print("-------------------------------------------------------------------------------------------------------\n",
              "Total execution time:- ", time() - start, sep="")

        return result

    # return the reference to the inner function
    return innerFunction
