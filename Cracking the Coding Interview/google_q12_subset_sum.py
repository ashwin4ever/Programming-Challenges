#subarray with given sum


#a = [1 , 2 , 3 , 7 , 5]
a = [10, 2, -2, -20, 10]

def subSetSum(a):

      s = 0

      target = -10
      res = []

      if len(a) == 0:
            return

      
      for i in range(len(a)):
            
            s += a[i]
            
            res.append((a[i] , i))
            
            if s == target:
                  print('found' , s)
                  return res

            elif s > target:
                  return subSetSum(a[1: ])



            
print(subSetSum(a))
