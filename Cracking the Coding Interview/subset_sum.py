#subset sum
a = [10, 3, 4, 20, 10]


def subsetSum(a):

      n = len(a)

      curSum = a[0]
      start = 0
      target = 10
      res = [(a[0] , 0)]


      for i in range(1 , n + 1):

            while (curSum > target and start < i - 1):
                  #print(res , curSum , start , i - 1)
                  curSum = curSum - a[start]
                  res.pop(0)
                  start += 1
                  #print(res , curSum , start , i - 1)
                  
            #print(res)
            if curSum == target:
                  
                  return res

            if i < n:
                  curSum += a[i]
                  res.append((a[i] , i))
                  

print(subsetSum(a))
