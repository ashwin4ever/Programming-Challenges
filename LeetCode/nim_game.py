#Nim Game


class Solution(object):


      def canWinNim(self , n):

            return True if n & 3 else False

            
                  
s = Solution()
n = 5
print(s.canWinNim(n))
