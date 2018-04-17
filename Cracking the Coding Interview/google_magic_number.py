#cube root number



def cubeRoot(n):
      return n ** (1. / 3.)



def findCubes(n):

      i = 1
      j = 1
      k = 1

      #cube = int(cubeRoot(1729))

      count = 1
      chk = 0

      while count < n:

            chk = 0
            
            for i in range(1 , int(cubeRoot(count)) + 1):
                  for j in range(i + 1 , int(cubeRoot(count)) + 1):

                        #print(i , j)

                        if pow(i , 3) + pow(j , 3) == count:
                              chk += 1
                              print(i , j , count , chk)

            count += 1

            if chk == 2:
                  break


      


findCubes(1730)                 
