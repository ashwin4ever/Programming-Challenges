#KMP Algorithm

def kmp(pat , txt):

      n = len(txt)
      m = len(pat)

      lps = [0] * m

      calcLPS(pat , lps)
      print(lps)

      i = 0
      j = 0

      while i < n:

            if pat[j] == txt[i]:

                  i += 1
                  j += 1

            if j == m:
                  print('Pattern found at : ' , i)

                  #reset j
                  j = lps[j - 1]


            elif i < n and pat[j] != txt[i]:

                  if j == 0:
                        i += 1
                  else:
                        j = lps[j - 1]
                  
                  
def calcLPS(pat , lps):

      i = 1
      j = 0

      lps[0] = 0

      while i < len(pat):

            if lps[j] == lps[i]:

                  lps[i] = j + 1
                  i += 1
                  j += 1
            else:
                  if j == 0:
                        
                        lps[i] = 0
                        i += 1
                  else:

                        j = lps[j - 1]



txt = "Mississippi"
pat = "is"

kmp(pat , txt)
