#Quick SOrt


def quickSort(arr , l , h):

      if l < h:

            p = partition(arr , l , h)

            quickSort(arr , l , p - 1)
            quickSort(arr , p + 1 , h)

def partition(arr , low , high):

      i = low - 1
      piv = arr[high]

      for j in range(low , high):

            if arr[j] <= piv:
                  i += 1
                  print(arr[j] , arr[i])
                  arr[i] , arr[j] = arr[j] , arr[i]

      #replace piv
      arr[i + 1] , arr[high] = arr[high] , arr[i + 1]

      return i + 1


a = [2 , 7 , 4 , 1 , 5 , 3]
quickSort(a , 0 , len(a) - 1)
print(a)
