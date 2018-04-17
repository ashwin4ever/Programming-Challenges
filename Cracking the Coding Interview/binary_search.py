#binary search

def binarySearch(arr , left , right , elm):

      if right >= 1:

            mid = left + (right - 1) // 2

            if arr[mid] == x:
                  return mid

            # if the elemnt is less than mid search left
            if arr[mid] > elm:
                  return binarySearch(arr , left , mid - 1 , elm)


            else:
                  return binarySearch(arr , mid + 1 , right , elm)


      return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 10

res = binarySearch(arr , 0 , len(arr) - 1 , 10)
print(res)
