#shortest path

from collections import defaultdict


class Graph:

      def __init__(self , vert):

            self.v = vert
            self.graph = defaultdict(list)



      def addEdge(self , u , v , w):
            self.graph[u].append((v , w))


      def topoSort(self , v , visited , stack):

            visited[v] = True

            if v in self.graph.keys():
                  for n , w in self.graph[v]:
                        self.topoSort(n , visited , stack)


            stack.append(v)


      def shortestPath(self , start):

            visited = [False] * self.v

            stack = []

            for i in range(self.v):

                  if visited[i] == False:
                        self.topoSort(s , visited , stack)


            dist = [float('inf')] * self.v

            dist[0] = 0

            while stack:

                  i = stack.pop()

                  for n , w in self.graph[i]:

                        if dist[n] > dist[i] + w:
                              dist[n] = dist[i] + w


g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
