#List alternate max and min


import math

def alterNate(arr):

      n = len(arr)

      arr.sort()

      for i in range(1 , math.ceil((n + 1) / 2)):
            print(i , 2 * i - 1)

            x = arr[-1]
            arr.pop()
           
            #arr[2 * i - 1] = x
            

      print(arr)



inp = [1, 3, 8, 2, 7, 5, 6, 4]
alterNate(inp)
