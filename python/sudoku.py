
def getBlockNumber(row, column):
 
 if row < 3:

  if column < 3:
   return 1
  if column < 6:
   return 4
  else:
   return 7
 
 if row < 6:

  if column < 3:
   return 2
  if column < 6:
   return 5
  else:
   return 8
 
 else:

  if column < 3:
   return 3
  if column < 6:
   return 6
  else:
   return 9
 

def getBlockKeep(value="", low=1, high=10):
 block = {n:value for n in range(low, high)}
 return block

def getSudokuTable(value=""):
 table = [[value for i in range(9)] for j in range(9)]
 return table

def sudokuValidate(table, row_num, col_num):

 for row in range(9):
  
  for col in range(9):
   
   number = table[row][col]
   if number != ".":
    
    if number in block[getBlockNumber(row, col)]:
     return "No"
    else:
     block[getBlockNumber(row, col)] += number
    
    if number in row_num[row]:
     return "No"
    else:
     row_num[row] += number

    if number in col_num[col]:
     return "No"
    else:
     col_num[col] += number
    
 return "Yes"

def printTable(table):
 for row in range(9):
  for col in range(9):
   print(table[row][col], end=" ")
  print()
 
repeat = int(input())

response = list()

while repeat > 0:

 block = getBlockKeep()

 table = getSudokuTable()

 row_number = getBlockKeep("", 0, 9)

 col_number = getBlockKeep("", 0, 9)

 for row in range(9):
  line = input().split()
  # print(len(line))
  for col in range(9):
   table[row][col] = line[col]

 printTable(table)
 print()
 response.append(sudokuValidate(table, row_number, col_number))

 repeat -= 1

for res in response:
 print(res)
