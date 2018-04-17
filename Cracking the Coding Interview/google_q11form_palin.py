#form a palindrome



def isPalin(s):

      letters = [0]* 128
      singleCount = 0

      #aba    
      for c in s:
            val = ord(c)
            letters[val] += 1

      for c in s:

            if letters[val] == 1:
                  singleCount += 1

            if singleCount > 1:
                  return False
      return True

def formPalin(s):

      #abcd

      if len(s) == 1 or s == '':
            return s

      if isPalin(s):
            print(s , 0)
            return True


      temp = s[0]
      i = 1
      

      while True:

            if temp[0] == s[-1]:
                  s = temp[0 : len(temp) - 1] + s
                  break

            temp = s[i : i + 1] + temp

            print(temp)
            i += 1

      print(s , i - 1)

      if isPalin(s):
            return True

      return False
      
            
print(formPalin('geeks'))
