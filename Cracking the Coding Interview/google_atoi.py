#Implement atoi
#Convert string to int


def isNumeric(x):

      if x >= '0' and x <= '9':
            return True
      return False

def atoi(s):

      if len(s) == 0:
            return 0

      res = 0
      sign = 1
      i = 0

      n = len(s)

      if s[0] == '-':
            sign = -1
            i += 1

      for k in range(i , n):

            if (isNumeric(s[k]) == False):
                  return 0

            res = res * 10 + (ord(s[k]) - ord('0'))

      return sign * res




s = '-&1234'

print(atoi(s))
