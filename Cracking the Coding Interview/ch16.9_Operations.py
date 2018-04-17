#16.9 Operations

def getMax(a , b):

      c = a - b

      k = (c >> 31) & 0x1

      m = a - k * c

      return m

def isPos(n):

      return not((n >> 31) & 0x1 or not n)


def subtract(a , b):

      m = getMax(a , b)
      #print(m)

      if m == a:
            return m + (~b + 1)
      else:
            return m + (~a + 1)

def divide(a , b):

      temp_a = abs(a)
      temp_b = abs(b)

      s = temp_b
      x = 0
      
      #10 , 5

      while s <= temp_a:
            s += temp_b
            x += 1

      return x


def multiply(a , b):

      if a == 0 or b == 0:
            return 0

      temp_a = abs(a)
      temp_b = abs(b)
      s = temp_a

      for i in range(1 , temp_b):
            s += temp_a

      #print(temp_a)

      if not isPos(a) or not isPos(b):
            return ~s + 1
      else:
            return s


print(subtract(10 , 8))
print(multiply(-10 , -8))
print(divide(10 , 2))
      
