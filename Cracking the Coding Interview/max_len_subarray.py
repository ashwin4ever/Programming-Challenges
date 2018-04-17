#Length of longest contiguous sub array



def findLen(arr):

      
      n = len(arr)

      mn , mx = 0 , 0
      max_len = 1

      for i in range(n - 1):

            mn , mx = arr[i] , arr[i]

            for j in range(i + 1 , n):

                  mn = min(mn , arr[j])
                  mx = max(mx , arr[j])

                  if ((mx - mn) == j - i):
                        max_len = max(max_len , mx - mn + 1)


      return max_len


arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
print(findLen(arr))

            
