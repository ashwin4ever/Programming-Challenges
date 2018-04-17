#detec cycles in graph



def cycle(g):

      color = {u : 'white' for u in g}

      found_cycle = [False]
      print(color)

      for u in g:
            if color[u] == "white":
                  dfs_visit(g , u , color , found_cycle)

            if found_cycle[0]:
                  break

      return found_cycle[0]

def dfs_visit(g , u , color , found_cycle):

      if found_cycle[0]:
            return

      color[u] = 'gray'

      for v in g[u]:

            if color[v] == 'gray':
                  found_cycle[0] = True
                  return

            if color[v] == 'white':
                  dfs_visit(g , v , color , found_cycle)

      color[u] = 'black'






graph = { 0 : [1],
                    1 : [2],
                    2 : [3],
                    3 : [4],
                    4 : [1] }

print(cycle(graph))
