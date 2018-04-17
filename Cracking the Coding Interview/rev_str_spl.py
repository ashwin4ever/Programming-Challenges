#reverse a string without affecting spl chars

import re

s = "Ab,c,de!$"

print(s)
alph_str = re.findall(r'(\w+)' , s)

print(alph_str)


i , j = 0 , len(alph_str)

while(i < len(s) and j > 0):

      #print(s[i] , i , j)
      if re.match(r'(\w+)' , s[i]) is not None:
            print(s[i] , '  ' , alph_str[j - 1][: : -1])
            s = s[ : i] + alph_str[j - 1][: : -1] + s[i + 1 : ]
            print(s)
            j -= 1

      i += 1
      
print()
print(s)
            
            


