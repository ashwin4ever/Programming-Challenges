#Keyboard row


class Solution(object):


      def findWords(self , words):

            r1 = set('qwertyuiop')
            r2 = set('asdfghjkl')
            r3 = set('zxcvbnm')

            return[w for w in words if any(set(w.lower()) <= r for r in (r1 , r2 , r3))]




s = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]

print(s.findWords(words))
