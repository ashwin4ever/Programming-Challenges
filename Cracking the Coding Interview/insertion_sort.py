#insertion sort


def insertionSort(arr):

      n = len(arr)
      j = 0

      for i in range(1 , n):

            key = arr[i]

            j = i - 1

            while (j >= 0 and key < arr[j]):
                  arr[j + 1] = arr[j]
                  j -= 1

            arr[j + 1] = key


      print(arr)

a = [2 , 7 , 4 , 1 , 5 , 3]
insertionSort(a)
