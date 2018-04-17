#minimum cut palindrome



def splitString(s):


      if s == '' or isPalindrome(s):
            print(s)
            return 0

      cuts = float('inf')

      #cuts = min(1 + splitString(s[0 : 1]) + splitString(s[1: ]) , cuts)

      for i in range(len(s)):
            #pass
            #cuts = 1 + splitString(s[i + 1 : len(s)])
            cuts = min(1 + splitString(s[0 : i]) + splitString(s[i + 1 : len(s)]) , cuts)

      return cuts
            

def isPalindrome(s):

      n = len(s)
      #print(s)
      for i in range( n // 2):

            if s[i] != s[n - i - 1]:
                  #print('palin')
                  return False

      return True




s = "xabaay"

print(splitString(s))
