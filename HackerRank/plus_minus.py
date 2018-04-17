#Plus Minus

'''
Given an array of integers, calculate
which fraction of its elements are
positive, which fraction of
its elements are negative, and
which fraction of its elements
are zeroes, respectively.
Print the decimal value of
each fraction on a new line.
'''

n = int(input())
pos = 0
neg = 0
zero = 0
ctr = 0

nums = list(map(int , (input().split(' '))))

pos = len([x for x in nums if x > 0]) / n
neg = len([x for x in nums if x < 0]) / n
zero = len([x for x in nums if x == 0]) / n

#print(type(nums))

print(format(pos , ".6f"))
print(format(neg , ".6f"))
print(format(zero , ".6f"))



      
      
