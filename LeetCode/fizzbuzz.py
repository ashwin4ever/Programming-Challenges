#Fizz Buzz



class Solution(object):


      def fizzBuzz(self , n):

            res = []

            for i in range(1 , n + 1):


                  if i % 3 == 0 and not i % 5 == 0:
                        res.append("Fizz")

                  elif i % 5 == 0 and not i % 3 == 0:
                        res.append("Buzz")

                  elif i % 15 == 0:
                        res.append("FizzBuzz")

                  else:
                        res.append(str(i))

            return res


s = Solution()

n = 15

print(s.fizzBuzz(n))

                  
                        
            




