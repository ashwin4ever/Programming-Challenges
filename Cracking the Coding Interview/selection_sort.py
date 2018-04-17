#Selection sort


def selectionSort(arr):

      n = len(arr)

      for i in range(n - 1):
            imin = i

            for j in range(i + 1 , n):

                  if arr[j] < arr[imin]:
                        imin = j

            arr[i] , arr[imin] = arr[imin] , arr[i]


      print(arr)


a = [2 , 7 , 4 , 1 , 5 , 3]
selectionSort(a)
