#16.6 Smallest Difference



def mergeSort(arr):

      n = len(arr)

      if n > 1:

            mid = n // 2

            left = arr[0 : mid]

            right = arr[mid : ]

            mergeSort(left)
            mergeSort(right)

            combine(arr , left , right)


def combine(res , left , right):

      i = 0
      l = 0
      r = 0

      while l < len(left) and r < len(right):

            if left[l] < right[r]:
                  res[i] = left[l]
                  l += 1
            else:
                  res[i] = right[r]
                  r += 1
            i += 1

      while l < len(left):
            res[i] = left[l]
            i += 1
            l += 1

      while r < len(right):
            res[i] = right[r]
            i += 1
            r += 1


def findDiff(arr_a , arr_b):

      a = 0
      b = 0
      diff = float('inf')
      
      while (a < len(arr_a) and b < len(arr_b)):

            temp = abs(arr_a[a] - arr_b[b])

            if diff > temp:
                  diff = temp

            if arr_a[a] < arr_b[b]:
                  a += 1
            else:
                  b += 1

      return diff

a = [11 , 2 , 1 , 15]
b = [127 , 4 , 12 , 23 , 19 , 235]

mergeSort(a)
mergeSort(b)

print(a)
print(b)

print(findDiff(a , b))
            
