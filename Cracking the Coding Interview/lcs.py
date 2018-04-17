#Implement LCS


a = 'AGGTAB'
b = 'GXTXAYB'

l_a = len(a)
l_b = len(b)


def lcs(a , b , l_a , l_b):

      res = [[None] * (l_b + 1) for i in range(l_a + 1)]

      for i in range(l_a):
            for j in range(l_b):

                  if (i == 0 or j == 0):
                        res[i][j] = 0
                  elif a[i - 1] == b[j - 1]:
                        print(a[i - 1] , b [j - 1])
                        res[i][j] = res[i - 1][j - 1] + 1
                  else:
                        res[i][j] = max(res[i - 1][j] , res[i][j - 1])

      return res[i][j]

                        
print(lcs(a , b , l_a , l_b))
