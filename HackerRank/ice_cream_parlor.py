# HackerRank Practice
# Ice Cream Parlour

def solve(m , c):

      L = len(c)

      i = 0
      tgt = c[0]
      ans = [0]
      start = 0
      #print(m)
      for i in range(1 , L + 1):

            while(tgt > m and start < i - 1):
                  tgt -= c[start]
                  start += 1
                  ans.pop(0)
            
            if len(ans) > 1 and tgt == m:
                  return ' '.join(map(str , ans))

            if i < L:  
                  tgt += c[i]
                  ans.append(i)
                  print(tgt , i , c[i])


t = int(input().strip())
i = 0
result =[]

while(i < t):
      m = int(input().strip())
      n = int(input().strip())
      c = [int(x) for x in input().split(' ')]

      result.append(solve(m , c))
      i += 1

print(result)
