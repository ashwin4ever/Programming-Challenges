#word break 2



def hasWord(s):

      bag = ["mobile","samsung","sam","sung","man","mango",
            "icecream","and","go","i","like","ice","cream"]

      if s in bag:
            return True

      return False


def checkWordsRec(s):

      n = len(s)
      res = [False] * n
      marker = [0] * n

      if hasWord(s):
            #print(s)
            return s

      
      suf = ''
      pre = ''
      #check for prefix
      for  i in range(1 , n + 1):

            pre = s[0 : i]

            if hasWord(pre):

                  suf = checkWordsRec(s[i : n])

                  if len(suf) > 0:
                        return pre +  ' ' + suf



      return False



print(checkWordsRec('imobileandicecream'))

      
