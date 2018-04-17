#Disitnct Transfromations


A = "rabbbit"
B = "rabbit"

def countDistinct(A , B):

      res = [[0] * (len(B) + 1) for i in range(len(A) + 1)]


      

      res[0][0] = 1

      for i in range(1 , len(A) + 1):
            #set first col to 0
            res[i][0] = 0

      for i in range(1 , len(A) + 1):
            for j in range(1 , len(B) + 1):

                  if A[i - 1] == B[j - 1]:
                        res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
                  else:
                        res[i][j] = res[i - 1][j]

      print(res[i][j])
                        


countDistinct(A , B)
