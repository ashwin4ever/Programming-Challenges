#weighted uniform string


from collections import defaultdict



def isRepeated(k , r , alph):

      n = len(k)
      
      #aabba 2 6 1
      prev = ''

      count = 1

      for i in range(n):

            if prev == k[i]:
                  count += 1
                  #r[s[i] * count] = alph[s[i]] * count
                  temp = alph[k[i]] * count
                  r[temp] = 1
            else:
                  r[alph[k[i]]] = 1
                  count = 1

            prev = k[i]

      return r


s = input().strip()

n = int(input().strip())

res = []

r = defaultdict(int)

alph = dict([(chr(i) , i - ord('a') + 1) for i in range(97 , 123)])

r = isRepeated(s , defaultdict(int) , alph)

for i in range(n):

      x = int(input().strip())

      if r[x]:
            res.append('Yes')
      else:
            res.append('No')

for r in res:
      print(r)
      
      


