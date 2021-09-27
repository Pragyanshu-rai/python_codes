from datetime import date, datetime

def getDays(dateStr : str) -> int:
    """
        returns the number of days between the given date and jan 1 of the same given year.
    """

    dateStr = list(map(int, dateStr.strip(" ").split("/")))
    currentDate = datetime(dateStr[2], dateStr[1], dateStr[0])
    initDate = datetime(dateStr[2], 1, 1)

    return int(str(abs(currentDate-initDate)).split(" ")[0]) + 1


if __name__ == "__main__":
    
    dateStr = input()
    print(getDays(dateStr))