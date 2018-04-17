#Next Greater Element 1



class Solution(object):


      def nextGreaterElement(self , num1 , num2):

            res = []
            #num1 = num1[0 : len(num1) - 1]
            t = 0

            #found = False
            
            for x in num1:

                  idx = num2.index(x)

                  #print(x , idx)

                  for i in range(idx + 1 , len(num2)):

                        #print(i)

                        if num2[i] > x:
                              res.append(num2[i])
                              #found = True
                              break
                  else:
                        res.append(-1)




            #res.append(-1)
            return res
                        
                  
nums1 = [4,1 , 2]
nums2 = [1,3,4,2]
#nums1 = [1,3,5,2,4]
#nums2 = [6,5,4,3,2,1,7]

s = Solution()
print(s.nextGreaterElement(nums1 , nums2))
