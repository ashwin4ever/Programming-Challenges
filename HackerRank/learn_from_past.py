# Learning From the Past 


n = int(input())

days_sum = []

for i in range(n):
      nums = list(map(int , input().split(' ')))

      temp = sum(nums) - min(nums)
      days_sum.append(temp)


#print(days_sum)
print(max(days_sum))
