#find rotation count


def findRotationCount(arr):

      low = 0
      
      n = len(arr)
      high = n - 1

      while low <= high:

            if arr[low] <= arr[high]:
                  return low

            mid = (low + high) // 2
            nxt = (mid + 1) % n
            prev = (mid + n - 1) // 2

            if (arr[mid] <= arr[nxt]
                and
                arr[mid] <= arr[prev]):
                  return mid
            elif arr[mid] <= arr[high]:
                  high = mid - 1
            elif arr[mid] >= arr[low]:
                  low = mid + 1

      return -1

arr = [15 , 22 , 23 , 28 , 1 , 2 , 3 , 4 , 5]
print(findRotationCount(arr))
