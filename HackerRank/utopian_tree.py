#Utopian Tree


t = int(input())

h = 1
res = []

for i in range(t):
      c = int(input().strip())

      if c == 0:
            res.append(h)

     
      else:
            i = 1

            while i <= c:

                  if i & 1:
                        h *= 2
                  else:
                        h += 1
                  i += 1

            res.append(h)
            h = 1

for x in res:
      print(x)


            
