#weighted uniform strings



s = input()
n = int(input().strip())

c = 0

dic = {}

res = []

for i in range(0 , len(s)):

      if i == 0 or s[i] != s[i - 1]:
            w = ord(s[i]) - ord('a') + 1
      else:
            w = w + ord(s[i]) - ord('a') + 1

      dic[w] = 1


for i in range(n):
      x = int(input())

      if x in dic:
            res.append('Yes')
      else:
            res.append('No')


for r in res:
      print(r)
 
