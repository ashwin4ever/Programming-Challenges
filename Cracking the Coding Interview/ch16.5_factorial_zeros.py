#16.5 Factorial Zeros



def numZeros(n):

      c = 0

      for i in range(2 , n + 1):

            while i % 5 == 0:
                  c += 1
                  i = i // 5

      return c


def factZeros(n):

      c = 0

      if n < 0:
            return

      i = 5

      while (n // i > 0):
            c += n // i
            i *= 5

      return c

print(numZeros(25))

print(factZeros(25))
