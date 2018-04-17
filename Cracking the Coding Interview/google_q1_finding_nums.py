#google questions
#finding the numbers


from collections import defaultdict
from functools import reduce

arr = [1 , 2 , 3 , 2 , 1 , 4]
#arr = [2 , 1 , 3 , 2]

d = defaultdict(int)

for n in arr:
      d[n] += 1


print(d)
#res = sorted(d , key = d.values() , reverse = True)
res = sorted(d.items() , key = lambda x: x[1] , reverse = False)
print([res[i][0] for i in range(len(res)) if res[i][1] < 2])


def xorUnique(arr):

      f = lambda x , y : x ^ y

      xorList = reduce(f , arr)

      setBit = xorList & ~(xorList - 1)

      u1 , u2 = 0 , 0
      print(setBit)
      print([x for x in arr if x & setBit])

      #u1 = [u1 ^ x for x in arr if x & setBit]
      for i in arr:
            if i & setBit:
                  u1 = u1 ^ i
            else:
                  u2 = u2 ^ i
      print('u1: ' , u1)
      print('u2: ' , u2)

      #u2 = [u2 ^ y for y in arr if not (y & setBit)]


      
xorUnique(arr)      
