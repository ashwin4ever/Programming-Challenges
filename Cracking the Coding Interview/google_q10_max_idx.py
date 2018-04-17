#Maximum Index

from collections import deque

a = [3 , 5 , 4 , 2]

maxVal = -9999999

for i in range(len(a)):
      for j in range(i + 1 , len(a)):

            if (a[i] <= a[j]):
                  if (j - i) > maxVal:
                        maxVal = j - i




def maxInd(arr):

      lMin = deque()
      rMax = deque()

      minVal = 9999
      maxVal = -9999
      
      for i in  range(len(arr)):

            if (arr[i] < minVal):
                  minVal = arr[i]
                  lMin.append((arr[i] , i))
      print(lMin)

      for j in range(len(arr) - 1 , 0 , -1):

            if (arr[j] > maxVal):
                  maxVal = arr[j]
                  rMax.appendleft((arr[j] , j))
      print(rMax)

      diff = -1
      x , y = 0 , 0
      i , j = 0 , 0

      while lMin and rMax:

            x , i = lMin[0][0] , lMin[0][1]
            y , j = rMax[0][0] , rMax[0][1]

            if x < y:
                  if (j - i) > diff:
                        diff = j - i
                  rMax.popleft()
            else:
                  lMin.popleft()

      return diff


                 
                  
      


print(maxInd(a))
print(maxVal)
