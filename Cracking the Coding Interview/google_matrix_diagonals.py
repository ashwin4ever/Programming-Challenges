#print diagnoals of a matrix

import numpy as np


def printMatrix(arr):

      #print upper triangle 
      n = len(arr)
      row = 0

      while (row < n):
            col = 0

            temp = row

            while (temp >= 0):
                  print(arr[temp][col] , " " , end = '')
                  temp -= 1
                  col += 1

            print()
            row += 1


      #print lower triangle
      col = 1

      while (col < n):
            temp = col
            row = n - 1

            while(temp <= n - 1):
                  print(arr[row][temp] , ' ' , end = '')
                  row -= 1
                  temp += 1

            print()
            col += 1
      


arr = np.random.randint(5 , size = (5 , 5))
print(arr)

printMatrix(arr)
