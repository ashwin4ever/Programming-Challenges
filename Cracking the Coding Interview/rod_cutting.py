#rod cutting


def cutRod(arr , n):
      #print(n)

      if n <= 0:
            return 0

      max_price = -1


      for i in range(n):
            max_price = max(max_price , arr[i] + cutRod(arr , n - i - 1))

      return max_price


def cutRodDP(arr , n):

      val = [0] * (n + 1)

      for i in range(1 , n + 1):

            max_val = float('-inf')

            for j in range(i):
                  max_val = max(max_val , arr[j] + val[i - j - 1])

            val[i] = max_val

      return max_val


arr = [1, 5, 8, 9, 10, 17, 17, 20]
print(cutRodDP(arr , len(arr)))
