#longest common prefix


def getPrefix(s):

      
      s = s.split(' ')
      #Bedroom BedClock BedTable BedWall
      n = len(s)

      start = len(s[0])
      j = 0

      for i in range(1 , n):
            cur = 0
            j = 0

            while (cur < start and cur < len(s[i])):

                  if s[0][cur] == s[i][cur]:
                        #print(s[0][cur])
                        j += 1
                  cur += 1

            start = j

      print(s[0][0 : j])
            
      
      




s = "Bedroom BedClock BeTable BeWall"
getPrefix(s)
