#reverse a string without affecting spl chars

import re

s = "Ab,c,de!$"

print(s)

l , r = 0 , len(s) - 1

while (l < r):

      if re.match(r'(\w+)' , s[l]) is None:
            l += 1
      elif re.match(r'(\w+)' , s[r]) is None:
            r -= 1
      else:
            print('l: ' ,s[l] , ' ' ,s[ : r] + s[l] + s[r + 1 : ])
            print('r: ' ,s[r] , ' ' , s[ : l] + s[r] + s[l + 1 : ])
            s = s[ : l] + s[r] + s[l + 1 : ]
            s = s[ : r] + s[l] + s[r + 1 : ]
            
            l += 1
            r -= 1

print(s)
            
            


