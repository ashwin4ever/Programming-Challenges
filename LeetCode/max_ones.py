#Max consecutive ones



class Solution(object):

       def findMaxConsecutiveOnes(self, nums):

             n = len(nums)
             prevMax = 0
             count = 0

             #[1,1,0,1,1,1]

             for i in range(n + 1):

                   if count > prevMax:
                         prevMax = count

                   #print(count , prevMax , i)

                   if i < n and nums[i]:
                         count += 1
                   else:
                        count = 0


             return prevMax




nums = [1,1,0,1,1,1]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))
