#Circular array rotation



inp = input().split(' ')
n , k , q = [int(x) for x in inp]
m = []
#print(n , k , q)

#n -- > num of ints in arrays
#k - num of rotations
#q - num of queries

arr = list(map(int , (input().split(' '))))
result = []

for i in range(q):
      m = int(input())

      k = k % n
      
      if k == n:
            result.append(arr[i])
      elif m < k:
            result.append(arr[n - k + m])
      elif m >= k:
            result.append(arr[m - k])

#print(result)
for a in result:
      print(a)
