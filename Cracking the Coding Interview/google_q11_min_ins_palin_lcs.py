#Minimum insertions for a palindrome
#LCS Solutions



def lcs(str_a , str_b , la , lb):

      lcs = [[None] * (lb + 1) for i in range(la + 1)]


      for i in range(la):
            for j in range(lb):

                  if (i == 0 or j == 0):
                        lcs[i][j] = 0

                  elif str_a[i - 1] == str_b[j]:
                        lcs[i][j] = lcs[i - 1][j - 1] + 1
                  else:
                        lcs[i][j] = max(lcs[i - 1][j] , lcs[i][j- 1])

      return lcs[i][j]



def minInsertions(s):

      n = len(s)

      rev = s[: : -1]

      i = lcs(s , rev , n , n)

      print(n - i)


minInsertions('geeks')
