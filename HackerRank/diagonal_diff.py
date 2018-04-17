#Diagonal Difference

'''Print the absolute difference between the
two sums of the matrix's diagonals as a single integer.
'''


n = int(input())

arr = []

d1 = 0
d2 = n - 1

sum1 = 0
sum2 = 0

for x in range(n):
      matrix = input().split(' ')
      #print(matrix[d1] , '  ' , matrix[d2])
      #print(d1 , '  ' , d2)
      sum1 = sum1 + int(matrix[d1])
      sum2 = sum2 + int(matrix[d2])
      

      d1 += 1
      d2 -= 1

print(abs(sum1 - sum2))


