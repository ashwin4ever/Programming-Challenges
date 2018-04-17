#count distinct subsequence


from collections import defaultdict

def count(s):

      l = []

      n = len(s)

      dp = [0] * (n + 1)
      #dp = [0]
      dp[0] = 1
      last = defaultdict(int)

      for i in range(1 , n + 1):

            #print(dp[i] , dp[i - 1] , i , last[s[i - 1]])
            dp[i] = 2 * dp[i  - 1]
            print(last)
            #print(s[i - 1])

            if (s[i - 1] in last):
                  print('true')
                  dp[i] = dp[i] - dp[last[s[i - 1]]]
            
            last[s[i - 1]] = i - 1    


            
            
      print(dp[n]) 
            
      
s = 'gffg'
count(s)
