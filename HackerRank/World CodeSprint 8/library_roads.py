#Roads and Libraries

import sys
import math

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
      #old_q = []
      global roadCount
      q.append(s)
      #old_q.append(s)
      visited[m.index(s)] = True


      while q:

            n = q.pop(0)
##            if len(old_q) != 0:
##                  old_n = old_q.pop(0)

            if n == d:
                  return True

            for i in l:
                  if i[0] == n:
                        #print(i[1])
                        if visited[m.index(i[1])] == False:
                              q.append(i[1])
                              visited[m.index(i[1])] = True
##                              if (n , i[1]) not in oldRoad:
##                                    print('road exists: ' , (n , i[1]))
##                                    roadCount += 1
##                                    oldRoad.add((n , i[1]))
##                        else:
##                              roadCount = 1
                              
      
      return False



def checkCycle(src , dest):

      s = set(src)
      d = set(dest)
      sidx = 0
      didx = 0
      if len(s) == len(src) and len(d) == len(dest):
            if src[0] == dest[len(dest) - 1]:
                  return True
            else:
                  for i in src:
                        if i in dest:
                              sidx = dest.index(i)
                              break
                  for j in dest:
                        if j in src:
                              didx = src.index(j)
                              break;

                  if sidx == didx:
                        return True
                              

      return False

if q >= 1:
      
      for i in range(q):

            reachable = []
            unreachable = []
            uRoads = []
            roads = []
            roadsReq = 0
            cityReq = 0
            inValid = False
            n , m , cl , cr = input().split(' ')
            n , m , cl , cr = [int(n),int(m),int(cl),int(cr)]

            if n <= 0 or m < 0 :
                  continue
            if cl <= 0 or cr <= 0:
                  continue
            if cl > pow(10 , 5) or cr > pow(10 , 5):
                  continue

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

                        if city_1 > n or city_2 > n:
                              inValid = True
                              break
                  
                  uniqueRoads = list(set(uRoads))
                  src = [x[0] for x in roads]
                  dest = [x[1] for x in roads]

                  #print(src)
                  #print(dest)

                  srcS = set(src)
                  destS = set(dest)
                  #print(srcS)
                  #print(destS)
                  inter = srcS.intersection(destS)

                  if srcS == destS and not inValid:
                        src = list(set(src))
                        dest = list(set(dest))
                        #print('hello')
                        pairCount = 0
                        pc = 0
                        if checkCycle(src , dest):
                              
                  
                              for i in srcS:
                                    for j in destS:
                                          if i != j:
                                                if not isReachable(roads , uniqueRoads , i , j):
                                                      if i == src[0]:
                                                            pairCount += 1

                              
      
                              #if pairCount > 0:
##                                    
##                                    if n % pairCount == 0:
##                                          pc = math.ceil(n / pairCount)
##                                    else:
##                                          pc = math.ceil(n / pairCount) + 1                                                      

                                    #pc = math.ceil(n / pairCount)
                              #print(pairCount)
                              if pairCount == 0:
                                    cost = (cl) + (cr * (m - 1))
                                    if n * cl < cost:
                                          cost = n * cl
                                    else:
                                          cost = cost
                                    min_cost.append(cost)
                                    
                              elif pairCount > 1:     
                                    pc = pairCount
                                    #print('pair count: ' , pc , pairCount)
                                    ct = math.ceil(math.sqrt(n))
                                    rd  = ct * 2
                                    cost = (ct * cl) + cr * (rd)

                                    if n * cl < cost:
                                          cost = n * cl
                                    else:
                                          cost = cost
                                    min_cost.append(cost)
                                    
                              elif m < n:
                                    road = m - 1
                                    city = n - road
                                    cost = cl * city + cr * (road)
                                          
                                    if n * cl < cost:
                                          cost = n * cl
                                          #print('n cl ', cost)
                                    
                              else:
                                    cost = cost
                                    #print(cost)
                                    min_cost.append(cost)
                                    
                        else:
                                    
                              cost = cl + (m - 1) * cr
                              if n * cl < cost:
                                    cost = n * cl
                              else:
                                    cost = cost
                                    
                              min_cost.append(cost)
                                          
            
                  elif not inValid:

                        pairs = len(inter)

                        if pairs == 0:
                            cityReq = n - m
                            roadsReq = m

                        elif m < n and pairs <= len(srcS) - 1:
                              #print('here')
                              pairCount = len(inter)
                              pc = 0
##                              for i in srcS:
##                                    for j in destS:
##                                          if i != j:
##                                                if not isReachable(roads , uniqueRoads , i , j):
##                                                      print(i ,  j)
##                                                      if i == src[0]:
##                                                            pairCount += 1
##                                                      else:
##                                                            break
                              #print(pairCount)
                              if pairCount > 0:
                                    pc = pairCount
##                                    if n % pairCount == 0:
##                                          pc = pairCount
##                                    else:
##                                          pc = math.ceil(n / pairCount) + 1
                                          
                                    roadsReq = n - pc
                                    cityReq = pc
                                    #print(n , pc , roadsReq , cityReq , pc)
            
                                    #cost = (pc * cl) + cr * (n - pc)
                                    
                              #print(roadsReq , cityReq , pc)
                        elif m < n and len(pairs) <= 1:
                              #print('m less n')
                              if pairs == 1:
                                    roadsReq = m
                                    cityReq = (n - m)
                              else:
                              
                                    roadsReq = m - 1
                                    cityReq = (n - m) + 1
                        
                        
                        else:
                              #print('m less')
                        
                              roadsReq = n - pairs
                              cityReq = pairs

                        if roadsReq == 0 and cityReq == 0 and m < n:
                              cityReq = n - m
                              roadsReq = m 
                              
                              #print(srcS , destS , roadsReq , cityReq)

                        totalLibCost = n * cl
                        totalRoadCost = m * cr
                  
                        roadCost = (roadsReq) * cr

                         
                        libCost = cityReq * cl

                  


                        #print(roadCost , libCost)
                  
                        totalCost = roadCost + libCost

                        if totalCost > totalLibCost:

                              min_cost.append(totalLibCost)
                        else:
                              min_cost.append(totalCost)
                        #print(min_cost)
     #print(min_cost)
      if len(min_cost) > 0:
            for c in min_cost:
                  print(c)                  
