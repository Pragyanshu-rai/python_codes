def fingersUp(number : str) -> str:
    
    if int(number) > 99 or int(number) < 0:
        return "-1"*10

    result = ['0']*10
    left = 0
    index = 9
    if len(number) == 2:
        left += 1
        index = 0 

    print(number)

    for digit in number:
        digit = int(digit)

        if digit > 5:
            digit -= 5
            mid = 5

            if left == 1:
                mid -= 1
            
            result[mid] = "1"
        
        while digit > 0:
            result[index] = "1"

            if left == 1:
                index += 1
            else:
                index -= 1
            
            digit -= 1

        index = 9
        left = 0

    return "".join(result)


if __name__ == "__main__":
    number = input()
    print(fingersUp(number))
    print(fingersUp("3"))
    print(fingersUp("8"))
    print(fingersUp("0"))
    print(fingersUp("99"))
    print(fingersUp("67"))
    print(fingersUp("83"))
    print(fingersUp("813"))
    print(fingersUp("-13"))