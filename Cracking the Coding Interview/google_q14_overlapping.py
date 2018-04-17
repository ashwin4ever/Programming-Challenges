#Overlapping Intervals



n = [int(x) for x in input().split(' ')]

print(n)

res = []
for j in range(0 , 8 , 2):
      print(j)
      res.append((n[j : j + 2]))

print(res)
#print(res[0][1])

def overLappingNums(res):

      #[[1, 3], [2, 4], [6, 8], [9, 10]]

      for i in 
