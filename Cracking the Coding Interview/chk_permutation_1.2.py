#Check Permutation:
#Given two strings, write a method to
#decide if one is a permutation of the
#other


def permutation(word):
      if len(word) <= 1:
            return word

      perm = permutation(word[1 : ])

      ch = word[0]

      result = []


      for p in perm:
            for i in range(len(p) + 1):
                  result.append(p[0 : i] + ch + p[i: ])

      return result

def isUnique(s):

      if len(s) >= 128:
            return False
      else:
            isSeen = [0] * 128
            for i in range(len(s)):
                  val = ord(s[i])

                  if isSeen[val] == 1:
                        return False
                  else:
                        isSeen[val] = 1
      return True

#print(permutation('abc'))

s1 = 'abc'
s2 = 'cbcabdabcdabcbca'

def checkIsPerm(s1 , s2):

      print(s1 , s2)

      letters = [0] * 128

      for c in s1:
            val = ord(c)
            letters[val] += 1


      for d in s2:
            val = ord(d)

            letters[val] -= 1

            if letters[val] < 0:
                  return False

      return True



                        
for i in range(len(s2)):
      print(checkIsPerm(s1 , s2[0 + i : i + 3]))





                  
 
