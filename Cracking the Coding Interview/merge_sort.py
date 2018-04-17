#merge sort




def mergeSort(arr):

      n = len(arr)

      if n > 1:

            mid = n // 2

            left = arr[0 : mid]
            right = arr[mid :]

            print(left , right)

            mergeSort(left)
            mergeSort(right)

            combine(arr , left , right)

def combine(res , left , right):

      i = 0
      l = 0
      r = 0
      #res = [0] * (len(left) + len(right))

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
            l += 1
            i += 1

      while r < len(right):
            res[i] = right[r]
            i += 1
            r += 1


a = [2 , 7 , 4 , 1 , 5 , 3]
mergeSort(a)
print(a)
      
