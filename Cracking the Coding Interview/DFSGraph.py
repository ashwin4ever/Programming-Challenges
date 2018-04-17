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

      def DFS(self , src):

            isVisited = [False] * self.vert

            self.dfsTrav(src , isVisited)

      def dfsTrav(self , src , visited):

            #mark cur node as visited
            visited[src] = True

            print('Node: ' , src)

            for adj in self.graph[src]:

                  if not visited[adj]:
                        self.dfsTrav(adj , visited)


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)

                              
            
