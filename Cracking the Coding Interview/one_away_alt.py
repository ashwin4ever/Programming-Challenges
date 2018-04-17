#One Away

import math


s1 = input().strip()
s2 = input().strip()


def checkEdit(s1 , s2):

      if math.abs(len(s1) - len(s2)) > 1:
            return False

      long = s1 if len(s1) > len(s2) else s2
      short = s1 if len(s1) < len(s2) else s2

      idx1 = 0
      idx2 = 0

      found = 0

      while idx1 < len(long) and idx2 < len(short):
            if long[idx1] != short[idx2]:
                  if found:
                        return False
                  found = 1

                  #if 
            

     
print(checkEdit(s1 , s2))
