#Bubble Sort



def bubbleSort(arr):
      n = len(arr)

      for i in range(n):

            flag = 0

            for j in range(0 , n - i - 1):

                  if arr[j] > arr[j + 1]:
                        arr[j] , arr[j + 1] = a[j + 1] , arr[j]
                        flag = 1
            if not flag:
                  break
                        

      print(arr)


a = [2 , 7 , 4 , 1 , 5 , 3]
bubbleSort(a)
