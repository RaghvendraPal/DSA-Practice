def undirected_path(edges, node_A, node_B):
  graph = create_graph(edges)
  print(graph)
  print(hasPathRecursion(graph, node_A, node_B))
#   return has_path(graph, node_A, node_B)
  
  
def create_graph(edges):
  graph = {}
  for edge in edges:
    i, j = edge
    if i not in graph: graph[i] = []
    if j not in graph: graph[j] = []
    
    graph[i].append(j)
    graph[j].append(i)
    
  return graph

def has_path(graph, src, dst):
  stack = [ src ]
  visited = [ src ]
  while len(stack):
    current = stack.pop()
    if current == dst:
      return True
    for val in graph[current]:
      if val not in visited:
        stack.append(val)
        visited.append(val)
      
  return False

def hasPathRecursion(graph, src, dst, visited = []):
    # print(visited)
    # if src in visited:
    #     return False
    if not visited:
        visited = [ src ]
    if src == dst:
        return True
    print(visited)
    for val in graph[src]:
        print(val)
        if val not in visited and hasPathRecursion(graph, val, dst, visited + [val]):
            return True

    return False

  
  
  
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'k', 'o')) # -> False

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'm', 'j'))
