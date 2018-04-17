#insertion sort



def insertionSort(arr):

      n = len(arr)

      #1 4 3 5 6 2

      k = 0

      for i in range(1 , n):

            key = arr[i]

            k = i - 1

            while k >= 0 and key < arr[k]:
                  arr[k + 1] = arr[k]
                  k -= 1

            arr[k + 1] = key
            printArr(arr)


def printArr(arr):

      for x in arr:
            print(x , end = ' ')

      print()


n = int(input())
arr = list(map(int , input().strip().split(' ')))
insertionSort(arr)
