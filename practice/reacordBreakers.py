from timer import getExecTime


@getExecTime
def getRecordsBroken(days: list = [1, 2, 0, 7, 2, 0, 2, 2]) -> int:
    """
        given an array of number of visitors it will return the number of record breaking days """

    broken = 0
    lastRecord = -1

    for day in range(len(days)):
        if (day == len(days)-1 and lastRecord < days[day]) or lastRecord < days[day] > days[day+1]:
            broken += 1
            lastRecord = days[day]
        # print(days[day], day) #show the days when a new records were set

    return broken


if __name__ == "__main__":
    print(getRecordsBroken())
