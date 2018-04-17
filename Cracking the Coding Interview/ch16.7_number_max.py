#16.7 max of number



def getMax(a , b):

      c = a - b

      #check if c is neg or pos

      k = (c >> 31) & 0x1

      m = a - k * c

      return m

def getMaxAlt(a , b):

      return ((a + b) + abs(a - b)) // 2

print(getMax(5 , 9))

print(getMaxAlt(10 , 9))
