#Angry Professor 

t = int(input())

res = []

for i in range(t):
      n , k = input().split(' ')
      n , k = int(n) , int(k)

      time = [int(x) for x in input().split(' ')]

      new_time = list(filter(lambda x: x <= 0 , time))
      #print(new_time)

      if len(new_time) < k:
            res.append('YES')
      else:
            res.append('NO')


for x in res:
      print(x)

      

      
