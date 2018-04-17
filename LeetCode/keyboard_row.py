#Keyboard row

class Solution(object):


      def findWords(self , words):

            row1 = 'qwertyuiop'
            row2 = 'asdfghjkl'
            row3 = 'zxcvbnm'

            res = []

            isFound = False

            for w in words:
                  for c in w:
                        #print(c)
                        if c.lower() not in row2:
                              isFound = False
                              break
                        else:
                              isFound = True
                  if not isFound:
                        continue
                  else:
                        res.append(w.strip())

            for w in words:
                  for c in w:
                        #print(c)
                        if c.lower() not in row1:
                              isFound = False
                              break
                        else:
                              isFound = True
                  if not isFound:
                        continue
                  else:
                        res.append(w.strip())


            for w in words:
                  for c in w:
                        #print(c)
                        if c.lower() not in row3:
                              isFound = False
                              break
                        else:
                              isFound = True
                  if not isFound:
                        continue
                  else:
                        res.append(w.strip())                        


            return res


s = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
#words = [x for x in input().strip().split(',')]
#print(words)
print(s.findWords(words))
            
                  
                        
            
