number = int(input())


def power_of_two(number):
    
    for k in range(70):
        
        if number == 1<<k :
            return 1
        
    return 0

print(power_of_two(number))
