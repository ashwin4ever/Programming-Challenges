#Sum of bit differences among all pairs


arr = [1 , 3 , 5]



def countBitDiff(arr):
      oneCount = 0
      zeroCount = 0

      res = 0

      for i in range(0 , 32):

            oneCount = 0
            zeroCount = 0

            for j in range(len(arr)):
                  if arr[j] & (1 << i):
                        oneCount += 1

            zeroCount = len(arr) - oneCount
            res += oneCount * zeroCount * 2

      print(res)


countBitDiff(arr)
