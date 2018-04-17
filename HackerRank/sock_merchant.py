#Sock Merchant


n = int(input())

socks = [int(x) for x in input().split(' ')]

sockCount = 0

d = {}

for i in socks:

      if i in d:
            d[i] += 1
      else:
            d[i] = 1

      if not d[i] & 1:
            sockCount += 1


print(sockCount)
