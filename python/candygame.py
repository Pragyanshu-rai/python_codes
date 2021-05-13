# Importing the randrange function to generate random numbers in a range
from random import randrange

# This function takes an array(list) as an argument an returns its int average
def averageInt(array):
  return sum(array)//len(array)

# This function will prompt the user for an integer input in the given range inclusive 
def getInt(lowLimit, uppLimit):

  number = int(input())
  
  if not (lowLimit <= number <= uppLimit):
    return None
  else:
    return number

# This function will prompt the user for an Even integer input in the given range inclusive 
def getEvenInt(lowLimit, uppLimit):

  # The getInt function is called and an valid input is taken and checked if it is even 
  number = getInt(lowLimit, uppLimit)
  if number == None or number % 2 != 0 :
    return None
  else:
    return number

# The Function that calls getInt and getEvenInt repeatedly until valid input is recieved 
def getValue(lowLimit, uppLimit, even=""):
  if even != "":
    even += " "
  # The prompt contains the string to ask the user
  prompt = "Enter an {}integer in [{}, {}] inclusive:".format(even, lowLimit, uppLimit)
  # This loop will run until a valid input is provided
  while True:
    
    print(prompt)
    # to an integer even or odd
    if even == "":
      number = getInt(lowLimit, uppLimit)

    else:
      even = "EVEN and "
      number = getEvenInt(lowLimit, uppLimit)
      
    if number == None:
      prompt = "Must be {}in [{}, {}] inclusive! re-enter:".format(even, lowLimit, uppLimit)
    else:
      return number

# This function takes two values as arguments and returns an even intger in range inclusive
def getEvenRandom(lowLimit, uppLimit):
  # The randrange function will genrate a random even number in range lowLimit to uppLimit inclusive by passing lowLimit, uppLimit+1 and step i.e 2  
  number = randrange(lowLimit, uppLimit+1, 2)
  return number

# This function takes an array as an argument and prints the values in aline with field width size 4, it returns nothing 
def printArray(students):
  for student in students:
    # Using %d for setting field width as 4
    print("%4d" %(student), end="")
  # for going to the next line 
  print()

# This function takes an array as an argument and passes half the value of previous elemt and adds it to the next element 
def passOutCandy(students):
  half = 0

  for index in range(len(students)):
    passing = half
    half = students[index] // 2
    students[index] //= 2
    if index > 0:
      students[index] += passing
  
  students[0] += half


# Creates the array of Students
def getStudents(size, lowLimit, uppLimit):
  students = [0]*size
  for index in range(len(students)):
    students[index] = getEvenRandom(lowLimit, uppLimit)
  
  return students 

# Deals Candy to each student if they have odd number of candies
def dealCandy(students):
  for index in range(len(students)):
    if students[index] % 2 != 0:
      students[index] += 1

# This function takes an array as an argument and checks if all the values are the same then returns true otherwise returns false
def gameOverTest(students):

  value = averageInt(students)

  for student in students:
    if value != student:
      return False

  return True

# Runs the game until every student has equal candies
def runGame(students, statusPrint=0):
  
  while not gameOverTest(students):
    passOutCandy(students)
    dealCandy(students)
    if statusPrint != 0:
      printArray(students)
  
  if statusPrint == 0:
    printArray(students)

# This function is the starting point and calls the appropriate functions 
def gameStart():
  lowLimit = 15
  uppLimit = 30
  print("Getting the number of students.")
  number = getValue(lowLimit, uppLimit)
  print("Getting the lower number of starting candy pieces from 4 to 10.")
  lowLimit = getValue(4, 10, even="even")
  print("Getting the upper number of starting candy pieces.")
  print("Must be even and greater than {} (the lower number) but less than or equal to {} (the lower number plus 50).".format(lowLimit, lowLimit+50))
  uppLimit = getValue(lowLimit+2, lowLimit+50, even="even")
  print("The original deal is:")
  students = getStudents(number, lowLimit, uppLimit)
  printArray(students)
  print("We are ready to play the game.\nDo you want to print the status after each move? (1 for yes, 0 for no)")
  response = getValue(0, 1)
  response = 1 # for testing,please comment this whole line when not testing
  runGame(students, response)

# Calling the gameStart function and stating the game
gameStart()
