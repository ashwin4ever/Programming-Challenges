#topological sorting


from collections import deque

def kahnSort(graph):

      in_deg = {u : 0 for u in graph}

      for u in graph:
            for v in graph[u]:
                  in_deg[v] += 1


      print(in_deg)
      q = deque()

      for u in in_deg:
            if in_deg[u] == 0:
                  q.appendleft(u)

      l = []
      print(q)

      while q:
            u = q.pop()
            l.append(u)

            for v in graph[u]:
                  print(v)
                  in_deg[v] -= 1

                  if in_deg[v] == 0:
                        q.appendleft(v)


      if len(l) == len(graph):
            return l
      else:
            return []
      




graph = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }



print(kahnSort(graph))
