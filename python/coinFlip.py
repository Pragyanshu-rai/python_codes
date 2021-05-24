def toggle(number):
 """
 arguments : number
 returns : 1 if number is 2 and 2 if number is 1
 """
 if number == 1:
  return 2
 return 1

def flip(init, coins, final):
 """
 arguments : init, coins, final
 returns : number of coins in final position
 """
 count = 0
 rounds = [init]*coins
 times = coins
 for index in range(coins):
  if times % 2 != 0:
   rounds[index] = toggle(rounds[index])
  if final == rounds[index]:
   count += 1 
  times -= 1
 return count 

repeat=int(input())
while repeat > 0 :
 game = int(input())
 while game > 0:
  inps = list(map(int, input().split()))
  print(flip(inps[0], inps[1], inps[2]))
  game -= 1
 repeat -= 1