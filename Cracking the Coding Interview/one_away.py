#One Away


s1 = input().strip()
s2 = input().strip()


def checkEdit(s1 , s2):

      if len(s1) == len(s2):
            return repl(s1 , s2)
      elif len(s1) == len(s2) + 1:
            return insert(s1 , s2)
      elif len(s1) == len(s2) - 1:
            return insert(s2 , s1)

      return False

def repl(s1 , s2):

      found = 0

      #pale , bale
      
      for i in range(len(s1)):
            if s1[i] != s2[i]:
                  if found:
                        return False

                  found = 1
      return True

#pale ple
def insert(s1 , s2):

      idx1 = 0
      idx2 = 0

      while idx1 < len(s1) and idx2 < len(s2) :
            if s1[idx1] != s2[idx2]:
                  if idx1 != idx2:
                        return False
                  idx1 += 1

            else:
                  idx1 += 1
                  idx2 += 1

      
      return True             
            
                  
print(checkEdit(s1 , s2))
