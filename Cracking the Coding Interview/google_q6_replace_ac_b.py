#remove 'ac' and 'b' from string


s = input()
n = len(s)

i = 0
j = 0
while i < n:

      if s[0] == 'b':
            s = s.replace(s[0] , '' , 1)
            i = 0
            n = n - 1
            #print('cut b: ' , s , i , n)

      if s[i] == 'b':
            s = s.replace(s[i] , '' , 1)
            i -= 1
            n -= 1

      if (i + 1) < n:
            if s[i] == 'a' and s[i + 1] == 'c':
                  s = s.replace('ac' , '' , 1)
                  i -= 2
                  n = n - 2

      i += 1
      #print(s , i)

      if n == 0 or n < 0:
            break

      
                  
            
print(s)
