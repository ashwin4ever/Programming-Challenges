# Hacker Rank Practice
# Birthday Chocolates



def solve(n , s , d , m):
      
      count = 0
      idx = 0

      while(idx <= n and m <= n):

            if sum(s[idx : m]) == d:
                  count += 1
                  idx += 1
                  m += 1
            else:
                  idx += 1
                  m += 1
      return count

n = int(input().strip())
s = list(map(int , input().strip().split(' ')))
d , m = input().strip().split(' ')
d , m = [int(d) , int(m)]

result = solve(n , s , d , m)

print(result)
