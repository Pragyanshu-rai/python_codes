def sumOfDigits(number):
 result=0
 while number > 0:
  result += number%10;
  number //= 10;
 return result

def divisibleBySix(number):

 if (number%10)%2 == 0 and sumOfDigits(number)%3 == 0:
  return True
 return False

def twoOrSix(number):
 moves = 0
 if number == 6:
  return 1
 if divisibleBySix(number) == True:
  return number//6
 else:
  return -1
 

repeat = int(input())

while repeat > 0:
 number = int(input())
 print(twoOrSix(number))
 repeat -= 1