#Reverse String



class Solution(object):


      def reverseString(self , s):

            return s[: : -1]



sol = Solution()

s = "hello"

print(sol.reverseString(s))

