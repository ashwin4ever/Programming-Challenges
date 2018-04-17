#URLify


s = "Mr John Smith     "
l = 13


for i in range(l):

      #print(s[i])
      if s[i] == ' ':
            print('found')
            s = s.replace(s[i] , '%20' , 1)
            #print(s)

print(s)
