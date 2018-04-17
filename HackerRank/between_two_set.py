#Between Two Sets


import math

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

numFactors = []
##
##for i in range(1 , int(math.sqrt(n)) + 1):
##      if n % i == 0:
##            #print('i: ' , i)
##            numFactors.append(i)
##
##            if i != n // i:
##                  #print(i , n , n // i)
##                  numFactors.append(n // i)

def gcd(a , b):
      #print('a: ' , a , 'b: ' , b)
      if b == 0:
            return a
      #print( b , a % b)
      return gcd(b , a % b)


def gcdAll(b):

      res = b[0]

      for i in b[1 : ]:
            res = gcd(res , i)

      return res

def lcm(a , b):
      return a * (b // gcd(a , b))

def lcmAll(a):

      res = a[0]

      for i in a[1 : ]:
            res = lcm(res , i)

      return res


            


lcm_val = lcmAll(a)
gcd_val = gcdAll(b)

#print(lcm_val , gcd_val)
count = 0

l = lcm_val

while l <= gcd_val:
      if gcd_val % l == 0:
            count += 1
      l += lcm_val

print(count)
##for i in range(lcm_val , int(math.sqrt(gcd_val)) + 1):
##      if gcd_val % i == 0:
##            #print('i: ' , i)
##            numFactors.append(i)
##
##            if i != gcd_val // i:
##                  #print(i , n , n // i)
##                  numFactors.append(gcd_val // i)


#print(numFactors)
