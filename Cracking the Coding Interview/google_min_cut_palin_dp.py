#min cut palindrome



def minCuts(s):

      n = len(s)

      palin = [[False for c in range(n)] for r in range(n)]

      #Build the palin table for use in DP
      #Single letter palindromes
      #every single letter is a palindrome
      for i in range(n):
            palin[i][i] = True

      #for two chars, check if 1st and 2nd match (if 'aba' chk a and b)
      for i in range(n - 1):

            if s[i] == s[i + 1]:
                  palin[i][i + 1] = True

      #for palims of len 3 to n , the first and last should match
      for cl in range(3 , n + 1):

            for i in range(n - cl + 1):

                  j = cl + i - 1

                  #check if first and last match
                  #if yes , then check if substr also matches
                  #i.e. strip the first and last chars and so on..
                  if s[i] == s[j] and palin[i + 1][j - 1]:
                        palin[i][j] = True


      cuts = [999] * n

      for i in range(n):

            temp = float('inf')

            if palin[0][i]:
                  cuts[i] = 0
            else:
                  for j in range(i):

                        if palin[j + 1][i] and temp > cuts[j] + 1:
                              temp = cuts[j] + 1

                  cuts[i] = temp

      return cuts[n - 1]



            
print(minCuts('banana'))
