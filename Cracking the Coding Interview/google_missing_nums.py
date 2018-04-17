#Missing numbers

def findMissingNums(arr):

      minNum = arr[0]
      maxNum = arr[len(arr) - 1]
      limit = 10

      i = 0
      res = ''

      while i < len(arr):

            if i < minNum:
                  res += str(i) + ' - ' + str(minNum - 1) + ' , '
                  print(res)
                  minNum = i

            if (i + 1) < len(arr):
                  diff = arr[i + 1] - arr[i]
                  print(diff)

                  if diff > 2:
                        res += str(arr[i] + 1) + ' - ' + str(arr[i + 1] - 1) + ' , '
                        #i = i + 1
                  else:
                        res += str(arr[i] + 1) + ' , '
            
            if (i + 1) == len(arr):
                  if arr[i] < limit:
                        res += str(arr[i] + 1) +  ' - ' + str(limit)

                                          
            #else:
            i += 1
      return res

      
arr = [3 , 10]

n = 5



print(findMissingNums(arr))
