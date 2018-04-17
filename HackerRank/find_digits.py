#find digits


t = int(input())

c = 0
res = []

for i in range(t):

      n = input().strip()

      temp = int(n)
      for i in n:
            if int(i) != 0:
                  if temp % int(i) == 0:
                        c += 1

      res.append(c)
      c = 0


for c in res:
      print(c)
                  
            
      
