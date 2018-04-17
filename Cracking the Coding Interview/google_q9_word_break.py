#Word break


def hasWord(s):

      bag = ["mobile","samsung","sam","sung","man","mango",
            "icecream","and","go","i","like","ice","cream"]

      if s in bag:
            return True

      return False


def checkWords(s):

      if len(s) == 0:
            return True


      for i in range(1 , len(s) + 1):

            print(s[i : len(s) - i])

            if hasWord(s[0 : i]) and checkWords(s[i : len(s)]):
                  return True

      return False


print(checkWords('ilike'))
