#Beautiful Days




def reverseNum(i):

      temp = ''

      while i > 0:

            temp += str(i % 10)
            i = i // 10

      return int(temp)


def chkBeautiful(i , rev , k):

      if not abs(i - rev) % k:
            return True
      

i , j , k = input().split(' ')

i , j , k = int(i) , int(j) , int(k)

count = 0

for i in range(i , j + 1):

      rev = reverseNum(i)
      #print(i , rev)
      if chkBeautiful(i , rev , k):
            count += 1


print(count)

      

