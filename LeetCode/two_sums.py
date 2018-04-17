#Two sums
#Given an array of integers, return indices
#of the two numbers such that they add up to a specific target.

from collections import defaultdict

class Solution(object):


      def twoSum(self , num , target):

            n = len(num)
            d = {}

            if len(num) <= 1:
                  return False
            
            #[2, 7, 11, 15]
            #[3 , 2, 4]
            #[-1,-2,-3,-4,-5]

            for i in range(n):

                  if num[i] in d:
                        return [d[num[i]] , i]
                  else:
                        d[target - num[i]] = i






s = Solution()
#num = [-1,-2,-3,-4,-5]
num = [-3,4,3,90]
#num = [2, 7, 11, 15]
#num = [3 , 2 , 4]
target = 0
print(s.twoSum(num , target))

                        
                        
                  
