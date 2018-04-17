#Mini-Max Sum

'''
Given five positive integers, find the minimum
and maximum values that can be
calculated by summing exactly
four of the five integers.
Then print the respective minimum and maximum values
as a single line of two space-separated long integers.
'''

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
#print(a , b, c , d, e)
arr = [a , b , c , d , e]
arr.sort()

#print(arr[min(arr) : 4])
min_sum = sum(arr[0 : 4])
max_sum = sum(arr[: 0 : -1])

print(min_sum , max_sum)

'''
Aletrnate and elegant:
lst = map(int,raw_input().strip().split(' '))
x = sum(lst)
print (x-(max(lst))), (x-(min(lst)))
'''


