#Roads and Libraries


q = int(input().strip())

roads = []
uniqueRoads = []
min_cost = []

reachable = []
unreachable = []
connected = False
roadCount = 0
oldRoad = set()
roadSet = set()


def isReachable(l , m , s , d):

      visited = [False] * (len(m))
      #print(visited)
      q = []
      old_q = []
      global roadCount
      q.append(s)
      old_q.append(s)
      visited[m.index(s)] = True


      while q:

            n = q.pop(0)
            if len(old_q) != 0:
                  old_n = old_q.pop(0)

            if n == d:
                  return True

            for i in l:
                  if i[0] == n:
                        #print(i[1])
                        if visited[m.index(i[1])] == False:
                              q.append(i[1])
                              visited[m.index(i[1])] = True
                              if (n , i[1]) not in oldRoad:
                                    print('road exists: ' , (n , i[1]))
                                    roadCount += 1
                                    oldRoad.add((n , i[1]))
                        else:
                              roadCount = 1
                              
      
      return False




def get_minimum_cost(roads , uniqueRoads ,cl , cr):

      lib_cost = cl * len(uniqueRoads)
      rep_cost = cr * (len(uniqueRoads) - 1)


      #print(lib_cost , rep_cost , cl , cr)
      
      if rep_cost > lib_cost:
            return lib_cost
      else:
            #print(cl + rep_cost)
            return cl + rep_cost

      return 0


for i in range(q):

      reachable = []
      unreachable = []
      uRoads = []
      n , m , cl , cr = input().split(' ')
      n , m , cl , cr = [int(n),int(m),int(cl),int(cr)]

      if m == 0:
            cost = n * cl
            min_cost.append(cost)

      else:
            for i in range(m):
                  
                  city_1 , city_2 = input().split(' ')
                  city_1 , city_2 = [int(city_1) , int(city_2)]

                  roads.append([city_1 , city_2])
                  uRoads.append(city_1)
                  uRoads.append(city_2)
            uniqueRoads = list(set(uRoads))
            src = [x[0] for x in roads]
            dest = [x[1] for x in roads]
            #print(n , len(uniqueRoads) , uniqueRoads)

            if len(uniqueRoads) < n:
                  #print('here')
                  min_cost.append(cl * (n - len(uniqueRoads)) + get_minimum_cost(n , uniqueRoads , cl , cr))
            elif len(uRoads) == len(uniqueRoads):
                  #print('equal')
                  min_cost.append(get_minimum_cost(n , uniqueRoads , cl , cr))
            else:
                  #min_cost.append(get_minimum_cost(n , uniqueRoads , cl , cr))
                  parent = 0
                  child = -1
                  h = set()
                  print(set(src))
                  print(set(dest))
                  if set(src) == set(dest):
                        min_cost.append((get_minimum_cost(n , set(src) , cl , cr)))
                  
                  else:
                        for i in set(src):
                       
                              for j in set(dest):
                              
                                    if i != j:
                                          #print(i , j , isReachable(roads , uniqueRoads , i , j))
                                          if isReachable(roads , uniqueRoads , i , j):
                                                print('pb: ' , parent , '  ' , 'childb: ' , child)
                                                if parent != i:
                                                      parent = i
                                                      print('pa: ' , parent , '  ' , 'childa: ' , child)
                                                      if child != parent:
                                                            child = j
                                                            reachable.append(i)
                                                            reachable.append(j)
                                                            print('pa: ' , parent , '  ' , 'childa: ' , child)
                                                            min_cost.append(sum([get_minimum_cost(n , set(reachable) , cl , cr)]))
                                                            print(i , j , '- ' , parent , child , get_minimum_cost(n , set(reachable) , cl , cr) , roadCount)
                                                            reachable = []
                                                                              
                                                
                                                
                                          else:
                                                unreachable.append((i , j))
                                                #print('un: ' , set(unreachable))
                                          #print('set: ' , h)
                   #get_minimum_cost(n , reachable , cl , cr)
                   #reachable = list(set(reachable))
##                  print(set(reachable) , set(unreachable))
##                  unreachable = list(set(unreachable))
##                  reachable = list(set(reachable) ^ set(unreachable))
##                  #unreachable = list(set(unreachable).intersection(set(reachable)))
##                  unreachable = list(set(reachable)- set(unreachable))
##                  print(reachable , unreachable)
##                  if len(unreachable) != 0 :
##                        #cost1 = get_minimum_cost(n , unreachable , cl , cr)
##                        if cl * len(unreachable) < cr * len(unreachable) - 1:
##                              cost1 = cl * len(unreachable)
##                        else:
##                              cost1 = (cl * len(unreachable)) - cr
##                        cost2 = get_minimum_cost(n , reachable , cl , cr)
##                        min_cost.append(sum([cost1 , cost2]))
##                  else:
##                        min_cost.append(get_minimum_cost(n , reachable , cl , cr))
                           
      


      
                  #min_cost.append(get_minimum_cost(roads , uniqueRoads , cl , cr))
                  #print(min_cost)


      
#print(roads , uniqueRoads)
#print(list(set(reachable)))
#print(list(set(unreachable)))

#print(min_cost)
for c in min_cost:
      print(c)
      
