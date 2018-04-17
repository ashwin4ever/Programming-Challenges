#Nuumber Complement


class Solution(object):


      def findComplement(self , num):

            c = 0
            m = 1

##            for i in range(32):
##
##                  if (m << i) & num:
##                        c = i


            c = num.bit_length()
            #print(num.bit_length())

            for i in range(c):

                  num = num ^ (1 << i)

            return num



 


            


s = Solution()
n = int(input())
print(s.findComplement(n))
