#Next Greater Element 1



class Solution(object):


      def nextGreaterElement(self , num1 , num2):

            d = {}
            st = []

            for x in num2:

                  while st and st[len(st) - 1] < x:
                        d[st.pop()] = x

                  st.append(x)

            return [d.get(x , -1) for x in num1]

            
                        
                  
nums1 = [4,1 , 2]
nums2 = [1,3,4,2]
#nums1 = [1,3,5,2,4]
#nums2 = [6,5,4,3,2,1,7]

s = Solution()
print(s.nextGreaterElement(nums1 , nums2))
