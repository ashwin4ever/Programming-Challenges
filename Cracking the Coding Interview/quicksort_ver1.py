# Quicksort example



def quickSort(arr , left , right):


      if left <  right:

            pivot = partition(arr , left , right)
            quickSort(arr , left , pivot - 1)
            quickSort(arr , pivot + 1 , right)


def partition(arr , l , r):

      piv = r

      wall = l

      while l < piv:

            if arr[l] < arr[piv]:
                  arr[wall] , arr[l] = arr[l] , arr[wall]
                  wall += 1
            l += 1

      arr[wall] , arr[piv] = arr[piv] , arr[wall]
      piv = wall
      return piv



a = [2 , 7 , 4 , 1 , 5 , 3]
quickSort(a , 0 , len(a) - 1)
print(a)
