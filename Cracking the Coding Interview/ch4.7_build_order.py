#Build order


from collections import defaultdict
from collections import deque

class Graph:

      def __init__(self):

            self.graph = defaultdict(list)


      def addEdge(self , src , dest):

            self.graph[src].append(dest)


      def getMaxOutdegree(self):

            res = {}

            for k , v in self.graph.items():
                  res[k] = len(list(v))
            print(res)
            maxNode = sorted(res , key = res.get , reverse = True)
            return maxNode

      def dfs(self , src):

            visited = defaultdict(int)
            for s in src:

                  q = deque()
                  if not visited[s]:
                        q.append(s)
                        visited[s] = True

                        while q:

                              curNode = q.popleft()

                              print('Node: ' , curNode)

                              for adj in self.graph[curNode]:

                                    if not visited[adj]:
                                          q.append(adj)
                                          visited[adj] = True




g = Graph()
g.addEdge('f' , 'c')
g.addEdge('f' , 'b')
g.addEdge('f' , 'a')
g.addEdge('a' , 'e')
g.addEdge('b' , 'e')
g.addEdge('b' , 'h')
g.addEdge('d' , 'g')


node = g.getMaxOutdegree()
print(node)
g.dfs(node)

            
            
