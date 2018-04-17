#Longest proper prefix sufix



def lps(s):

      i = 1
      j = 0

      lps = [0] * len(s)


      while (i < len(s)):


            if s[j] == s[i]:

                  lps[i] = j + 1
                  i += 1
                  j += 1
            else:
                  if j == 0:
                        lps[i] = 0
                        i += 1

                  else:
                        j = lps[j - 1]
      print(lps)

lps('ababa')
