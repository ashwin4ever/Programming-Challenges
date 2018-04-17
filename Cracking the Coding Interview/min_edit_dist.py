#Get minimum edit distance



def getMinEditDist(src , tgt):

      dist = [[None for j in range(len(tgt) + 1)] for i in range(len(src) + 1)]

      n1 = len(src)
      n2 = len(tgt)

      for i in range(n1 + 1):
            for j in range(n2 + 1):

                  #check and fill for empty string
                  #if src is empty
                  if i == 0:
                        dist[i][j] = j

                  #if col is empty
                  elif j == 0:
                        dist[i][j] = i

                  #if the chars at end match, then chk for 2nd to last
                  elif src[i - 1] == tgt[j - 1]:
                        dist[i][j] = dist[i - 1][j - 1]

                  else:
                        #if the chars are different
                        dist[i][j] = 1 + min(dist[i-1][j-1] , dist[i][j - 1] , dist[i - 1][j])

      return dist[n1][n2]



print(getMinEditDist('hackerhappy' , 'hackerrank'))
print(getMinEditDist('hackerrank' , 'hackerhappy'))
