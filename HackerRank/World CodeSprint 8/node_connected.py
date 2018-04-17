#find if a node is connected or not

#l = [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6] , [5 , 7]]
l = [[1, 2], [3 , 4] , [5 , 6]]


def isReachable(l , m , s , d):

      visited = [False] * (len(m))
      #print(visited)
      q = []

      q.append(s)
      visited[m.index(s)] = True


      while q:

            n = q.pop(0)

            if n == d:
                  return True

            for i in l:
                  if i[0] == n:
                        #print(i[1])
                        if visited[m.index(i[1])] == False:
                              q.append(i[1])
                              visited[m.index(i[1])] = True
      return False

m = [1, 2, 3, 4 , 5 , 6]
re = []
nr = []
for i in m:
      for j in range(i + 1 , len(m) + 1):
            print(i , j , isReachable(l , m , i , j))
            if isReachable(l , m , i , j):
                  re.append(i)
                  re.append(j)
            else:
                  nr.append(j)
print(len(l))
print(list(set(re)))
print(list(set(nr)))
                  
                  
