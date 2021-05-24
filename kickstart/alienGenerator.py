def generatesGBars(initBar, G):
 totalBars = 0
 while totalBars <= G:
  totalBars += initBar
  initBar += 1
  # print(totalBars)
  if totalBars == G:
   return True
   
 return False

def getBars(G):
 count = 0;
 for initBar in range(1, G+1):
  # print(initBar)
  if generatesGBars(initBar, G) == True:
   count += 1; 
   print(count, initBar, G)
 return count

def output(id, G):
 count = getBars(G)
 print("Case #{}: {}".format(id, count));

repeat = int(input())
id=1

while repeat > 0:
 
 g = int(input())
 output(id, g)
 
 id += 1
 repeat -= 1