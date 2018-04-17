#weighted uniform strings

from collections import defaultdict

##def chkUniform(alph , x , r):
##
##      #abccddde
##      #print(r , x)
##
##      chk = False
##
##      l = r[x]
##      #print(l)
##
##      if l != 0:
##            chk = True
##
##      return chk

def isRepeated(s , r , alph):

      n = len(s)
      
      #aabba 2 6 1
      prev = ''

      count = 1

      for i in range(n):

            if s[i] in alph:

                  if prev == s[i]:
                        count += 1
                        #r[s[i] * count] = alph[s[i]] * count
                        temp = alph[s[i]] * count
                        r[temp] = s[i] * count
                  else:

                        r[alph[s[i]]] = s[i]
                        count = 1

                  prev = s[i]
            else:
                  break

      return r


s = input().strip()

n = int(input().strip())

res = []

d = defaultdict(int)
#alph = defaultdict(int)

if len(s) >= 1 and n >= 1:
      
      alph = dict([(chr(i) , i - ord('a') + 1) for i in range(97 , 123)])

      r = isRepeated(s , defaultdict(int) , alph)

      ##d = prepDict(d , s)
      #print(r)

      for i in range(n):

            x = int(input().strip())

            if x >= 1:

                  if r[x]:
                        res.append('Yes')
                  else:
                        res.append('No')
            else:
                  break

      if len(res) >= 1:
            for r in res:
                  print(r)


      
