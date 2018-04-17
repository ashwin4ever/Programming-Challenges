#re arrange positive and negative numbers



def arrange(arr):

      n = len(arr)

      res = []

      i = 0

      while i < n:

            if arr[i] < 0:
                  res.append(arr[i])
                  del arr[i]
                  n -= 1

            i += 1

      arr.extend(res)
      print(arr)



def split(arr):

      n = len(arr)

      #print(arr)

      if n > 1:

            mid = n // 2

            left = arr[0 : mid]
            right = arr[mid : ]

            split(left)
            split(right)


            merge(arr , left , right)

def merge(arr , left , right):
      

      l = 0
      r = 0
      i = 0

      while l < len(left) and left[l] < 0:
            arr[i] = left[l]
            i += 1
            l += 1

      while r < len(right) and right[r] < 0:
            arr[i] = right[r]
            i += 1
            r += 1

      while l < len(left):
            arr[i] = left[l]
            i += 1
            l += 1

      while r < len(right):
            arr[i] = right[r]
            i += 1
            r += 1
      





      #left.extend(right)
      #arr.extend(left)
      
num = [1 , -2 , 3 , -4]

#arrange(num)
split(num)
print(num)
