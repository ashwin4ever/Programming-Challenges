#egg dropping puzzle




eggs = 2
floors = 10


def eggDropRecur(e , f):

      #if floors is 0 or 1 and we have eggs left
      #return floors
      if f == 0 or f  == 1:
            return f

      #if egss is none or zero , then return floors
      if e == 1:
            return f

      minVal = float('inf')
      res = 0

      for x in range(1 , f + 1):
            print(res , x)
            res = max(eggDropRecur(e - 1 , x - 1) , eggDropRecur(e , f - x))
            
            if (res < minVal):
                  minVal = res

      print(minVal)



def eggDropDP(eggs , floors):

      res = [[0 for r in range(floors + 1)] for i in range(eggs + 1)]

      #if floor is 0 or 1 we have to return floor
      for i in range(1 , eggs + 1):
            res[i][0] = 0
            res[i][1] = 1

      #if eggs is one return floor
      for j in range(1 , floors + 1):
            res[1][j] = j


      

      for i in range(2 , eggs + 1):
            for j in range(2 , floors + 1):
                  res[i][j] = float('inf')

                  for x in range(1 , j + 1):
                        ans = 1 + max(res[i - 1][x - 1] , res[i][j - x])

                        if ans < res[i][j]:
                              res[i][j] = ans
      return res[eggs][floors]

                  
#eggDropRecur(eggs , floors)


print(eggDropDP(eggs , 36))
