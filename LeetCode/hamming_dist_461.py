#Hamming distance



class Solution(object):

      def hammingDistance(self , x , y):

            #bit size
            n = 32
      
            i , j = 0 , 0
            c = 0

            chk_x = 0
            chk_y = 0

            while i < n and j < n:

                  chk_x = x & (1 << i)

                  chk_y = y & (1 << j)
                  #print(chk_x , chk_y)

                  if chk_x != chk_y:
                        c += 1

                  i += 1
                  j += 1

            return c
x = 93
y = 73
s = Solution()
print(s.hammingDistance(x , y))
      
