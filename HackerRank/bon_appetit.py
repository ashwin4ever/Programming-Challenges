#Bon Appetit

import functools

n , k = input().split(' ')
n , k = int(n) , int(k)


cost = [int(x) for x in input().split(' ')]
charged = int(input())

del cost[k]

orig_cost = sum(cost) // 2

overflow = charged - orig_cost

if overflow > 0:
      print(overflow)
else:
      print('Bon Appetit')
