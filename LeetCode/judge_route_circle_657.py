# Leet Code
# 657. Judge Route Circle


class Solution(object):

      def judgeCircle(self , moves):


            #x_s , y_s = moves.upper()

            x , y = 0 , 0
            

            dirs = {'U': (0 , 1) , 'D' : (0 , -1) , 'L' : (-1 , 0) , 'R': (1 , 0)}
            
            for d in moves:
                  #print(d , dirs[d])

                  x += dirs[d][0]
                  y += dirs[d][1]


            #print(x , y)
            if (x , y) == (0 , 0):
                  return True

            return False





moves = 'RL'

s = Solution()

print(s.judgeCircle(moves))
