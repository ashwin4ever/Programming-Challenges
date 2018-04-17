#Insertion sort part 1


def insertElement(arr):

      n = len(arr)

      e = arr[-1]

      #2 4 6 8 3

      i = n - 1
      k = 0

      while i > 0:      

            if arr[i - 1] > e:

                  k = i - 1               
                  arr[i]  = arr[i - 1]
                  printArr(arr)

                  
            i -= 1

      arr[k] = e
      printArr(arr)

def printArr(arr):

      for x in arr:
            print(x , end = ' ')

      print()



n = int(input())

arr = list(map(int , input().strip().split(' ')))

insertElement(arr)

      


                  

            
            
