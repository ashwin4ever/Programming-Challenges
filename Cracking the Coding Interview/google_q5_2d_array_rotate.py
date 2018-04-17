#rotate 2d array


inp = '7 4 1 8 5 2 9 6 3'
arr = [[7 , 4 , 1] , [8 , 5 , 2] , [9 , 6 , 3]]

print(len(arr))


def rotateMatrix(arr):

      n = len(arr)

      for i in range(n // 2):
            for j in range((n + 1) // 2):

                  temp = arr[i][j]

                  #top = left
                  arr[i][j] = arr[n - 1 - j][i]

                  #left = bottom
                  arr[n - 1 - j][i] = arr[n - 1 -i][n - 1 - j]

                  #bottom = right
                  arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][n - 1 - i]

                  #right = top
                  arr[j][n - 1 - i] = temp

      return arr


print(rotateMatrix(arr))
            
                  

      
