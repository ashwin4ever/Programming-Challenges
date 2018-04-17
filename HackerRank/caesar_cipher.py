# Hacker Rank Practice
# Caesar Cipher


def solve(n , s , k):

      res = ''
      temp = ''
      for c in s:
            k = k % 26
            if not c.isalpha():
                  res += c
            else:
                  if c.isupper():
                        if ord(c) + k > 90:
                              temp = chr(((ord(c) + k) % ord('Z')) + ord('A') - 1)
                        else:
                              temp = chr(ord(c) + k)
                              
                  else:
                        if ord(c) + k > 122:
                              temp = chr(((ord(c) + k) % ord('z')) + ord('a') - 1)
                        else:
                              temp = chr(ord(c) + k)

                  res += temp
                              
                        

      return res


n = int(input().strip())
s = input().strip()
k = int(input().strip())


result = solve(n , s , k)
print(result)
