# Hacker Rank Practice
# Two Characters

import re

def solve(n , s):

      uniq = list(set(s))
      #print(uniq)
      temp = ''

      len_res = []
      flag = False
      find = ''
      res = 0
      temp = ''

      for i in range(len(uniq)):
            for j in range(i + 1 , len(uniq)):


                   l = [c for c in s if c == uniq[i] or c == uniq[j]]
                   t = ''.join(l)
                   #print('t: ' , t , uniq[i] , uniq[j])

                   if checkPattern(t):
                         res = max(res , len(t))
                   

      return res

      
##      if len(s) == 2:
##            flag = checkPattern(s)
##
##      if not flag:
##
##            for i in range(len(uniq)):
##                  for j in range(i + 1 , len(uniq)):
##                        find = uniq[i] + uniq[j]
##                        temp = re.sub(r'['+str(find)+']' , '' , s)
##                        print(temp , find)
##                        #if len(set(temp)) == 2:
##                        print('Checking... ' , temp)
##                        if checkPattern(temp):
##                              print('right for: ' , temp)
##                              len_res.append(len(temp))      
##      else:
##            len_res.append(len(s))
##
##      print(len_res)
##      return 0 if len(len_res) == 0 else max(len_res)


def checkPattern(s):

      L = len(s)
      i = 0

      while(i < L):
            if i + 1 < L:
                  if s[i] == s[i + 1]:
                        return False
            i += 1

      return True
                        


n = int(input().strip())
s = input().strip()

result = solve(n , s)
print(result)
