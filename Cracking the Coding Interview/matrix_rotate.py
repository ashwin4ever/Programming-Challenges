#Rotate Matrix


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

      #rotMatrix = [[0] * len(matrix[0])] * len(matrix)
      n = len(matrix)

      rotMatrix = [[0 for i in range(n)] for i in range(n)]
      
      #print(matrix)
      for i in range(n):
            
            for j in range(n):
                  #print(matrix[n - j - 1][i])
                  rotMatrix[i][j] = matrix[n - j - 1][i]
                  #print(rotMatrix ,i , j)


      return rotMatrix  


m = generateMatrix(3)

print(m , len(m) , len(m[0]))
print(rotateMatrix(m))
                  
