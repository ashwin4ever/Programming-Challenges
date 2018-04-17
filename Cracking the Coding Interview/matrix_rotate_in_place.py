#rotate a matrix in place

import math

def generateMatrix(n):
      
      size = n
      matrix = []
      
      for i in range(n):
            
            inside = []
            
            for j in range(n):
                  inside.append(j + i * 2)

            matrix.append(inside)

      return matrix

def rotateMatrix(matrix):

      n = len(matrix)

      for i in range( (n // 2)):

            for j in range( (n + 1) // 2):

                  #save top in temp

                  temp = matrix[i][j]
                  print('top: ' , temp , i , j , n - 1 - i)

                  #top = left
                  matrix[i][j] = matrix[n - 1 - j][i]

                  #left = bottom
                  matrix[n - 1 - j][i] = matrix[n- 1 - i][n - 1 - j]

                  #bottom = right
                  matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

                  #right = top
                  matrix[j][n - 1 - i] = temp

                  #print(matrix)

      return matrix



m = generateMatrix(4)
print(m)

r = rotateMatrix(m)


print(r)
      
