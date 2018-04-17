#String Compression


s = 'aabccaa'

def compress(s):

      res = ''
      digits = 0

      for i in range(len(s)):
            digits += 1

            print(i)

            if i + 1 >= len(s) or s[i] != s[i + 1]:
                  res += '' + s[i] + str(digits)
                  digits = 0


      print(res)

      
      
                  
compress(s)
