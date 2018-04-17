#Route between nodes

'''Route Between Nodes: Given a directed graph,
design an algorithm to find out whether there is a
route between two nodes'''

from collections import defaultdict
from collections import deque

class Graph:

      def __init__(self , numVert):
            self.graph = defaultdict(list)

            self.vert = numVert

      #add edge to the graph 
      def addEdge(self , src , dest):
            self.graph[src].append(dest)

      def isReachable(self , src):

            isVisited = [False] * self.vert

            q = deque()
            q.append(src)

            isVisited[src] = True

            #while there are nodes left
            while q:
                  
                  #pop the node and traverse its adj nodes
                  curNode = q.popleft()

                  print('Node Visiting: ' , curNode)

                  for adj in self.graph[curNode]:

                        if not isVisited[adj]:
                              q.append(adj)
                              isVisited[adj] = True


g = Graph(6)
g.addEdge(0 , 5)
g.addEdge(0 , 4)
g.addEdge(0 , 1)
g.addEdge(1 , 4)
g.addEdge(1 , 3)
g.addEdge(2 , 1)
g.addEdge(3 , 4)
g.addEdge(3 , 2)

g.isReachable(0)

                              
            
