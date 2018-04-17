#Divisible Sum Pairs




n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

l = [(i , j) for i in range(len(a)) for  j in range(i + 1 , len(a)) if (a[i] + a[j]) % k == 0]

#d = [(i , j) for i in a for j in a[1 : ]]

#print(d)
#print(l)

print(len(l))
