#Palindrome Permutation



s = 'Tact Coobea'


def isPalinPerm(s):

      s = s.replace(' ' , '').lower()
      letters = [0] * 128
      singleCount = 0

      for c in s:
            val = ord(c)
            letters[val] += 1


      print(letters)

      for c in s:
            val = ord(c)

            if letters[val] == 1:
                  singleCount += 1

            if singleCount > 1:
                  return False

      return True

print(isPalinPerm(s))
            
