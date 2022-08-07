# undirected path
# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
# The function should return a boolean indicating whether or not there exists a path between node_A and node_B.


def adjancy_list(edges):
    dict1 = {}
    for i, j in edges:
        if i in dict1.keys():
            dict1[i].append(j)
        else:
            dict1[i] = [j]
        if j in dict1.keys():
            dict1[j].append(i)
        else:
            dict1[j] = [i]

    return dict1


# def undirected_path(edges, source, destination):

#     visited = [source]
#     data_queue = [source]
#     while data_queue:
#         current_data = data_queue.pop(0)
#         visited.append(current_data)
#         for value in edges[current_data]:
#             if value == destination:
#                 return True
#             if value not in visited:
#                 data_queue.append(value)

#     return False

def undirected_path(edges, source, destination, visited = None):

    if visited == None:
        visited = []

    if source == destination:
        return True

    if source in visited:
        return False

    visited.append(source)
    # print(visited)
    for val in edges[source]:
        if undirected_path(edges, val, destination, visited):
            return True

    return False


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'j', 'm')) # -> True

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'm', 'j')) # -> True

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'l', 'j')) # -> True

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'k', 'o')) # -> False

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'i', 'o')) # -> False

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'a', 'b')) # -> True

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'a', 'c')) # -> True

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'r', 't')) # -> True

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'r', 'b')) # -> False

edges = [
  ('s', 'r'),
  ('t', 'q'),
  ('q', 'r'),
]

edges = adjancy_list(edges)
print(undirected_path(edges, 'r', 't')) # -> True