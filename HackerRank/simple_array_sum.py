#Simple Array Sum
#Print the sum of the array's elements as a single integer.



def array_sum(arr):
      return sum(arr)


#limit = int(input())

n = int(input())

arr = [int(x) for x in input().split(' ')]

print(sum(arr))

#print(array_sum(arr))
