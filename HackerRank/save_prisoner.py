#Save the prisoner


t = int(input())

res = []

for i in range(t):

      n , m , s = map(int , input().split(' '))

      chkID = (s + m - 1) % n

      if chkID == 0:
            chkID = n

      res.append(chkID)

for j in res:
      print(j)



      
      
