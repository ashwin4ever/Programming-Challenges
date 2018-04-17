#Staircase

#Print a staircase of size using # symbols and spaces

n = int(input())

ctr = n
i = 1

char = '#'

for x in range(n):
      print((char * i).rjust(n))
      i += 1

