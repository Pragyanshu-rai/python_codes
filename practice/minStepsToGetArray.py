from Timers.timer import getExecTime


@getExecTime
def getMinSteps(target: list = [2, 3]) -> int:
    """
        returns the minimum number of steps required to genrate the given array
    """

    steps = 0

    while max(target) != 0:

        for index in range(len(target)):

            if target[index] & 1 == 1:
                target[index] -= 1
                steps += 1

        if max(target) == 0:
            return steps

        for index in range(len(target)):
            target[index] //= 2

        steps += 1


if __name__ == "__main__":
    print(getMinSteps())
    print(getMinSteps([2, 1]))
    print(getMinSteps([16, 16, 16]))
