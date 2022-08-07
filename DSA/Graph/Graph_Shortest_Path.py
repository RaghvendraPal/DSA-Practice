# shortest path
# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
# The function should return the length of the shortest path between A and B. Consider the length as the number of edges 
# in the path, not the number of nodes. If there is no path between A and B, then return -1.
from itertools import count
from numpy import Infinity


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


def shortest_path(edges, node_A, node_B):
    edges = adjancy_list(edges)
    path = Infinity
    # for val in edges[node_A]:
    visited = []
    path_size = explore_shortest_path(edges, node_A, node_A, node_B, visited)
    if path_size < path:
        path = path_size

    # if path == -1:
    print("Shortest Path : ", path)
    return path
    # else:
    #     print("Shortest Path : ", path-1)
    #     return path-1


def explore_shortest_path(edges, val, node_A, node_B, visited = None):
    # print("before : ",visited)
    if visited == None:
        visited = []
    if node_A == node_B:
        return 0
    count_re = -1
    for value in edges[node_A]:
        if value not in visited:
            v = explore_shortest_path(edges, value, value, node_B, visited+[node_A]) + 1
            if v:
                if count_re > v or count_re == -1:
                    count_re = v

    # print("after : ",visited)

    # print(val, count_re)

    return count_re

  





edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'w', 'z') # -> 2

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'y', 'x') # -> 1

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]
# print(adjancy_list(edges))
# {
#     'a': ['c', 'b'], 
#     'c': ['a', 'b', 'd'], 
#     'b': ['a', 'c', 'd'], 
#     'd': ['c', 'b', 'e'], 
#     'e': ['d'], 
#     'g': ['f'], 
#     'f': ['g']
# }
shortest_path(edges, 'a', 'e') # -> 3

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

shortest_path(edges, 'e', 'c') # -> 2

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

shortest_path(edges, 'b', 'g') # -> -1

edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

shortest_path(edges, 'w', 'e') # -> 1

edges = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
]

shortest_path(edges, 'n', 'e') # -> 2

edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

shortest_path(edges, 'm', 's') # -> 6
# {
#     'w': ['x', 'v'], 
#     'x': ['w', 'y'], 
#     'y': ['x', 'z'], 
#     'z': ['y', 'v'], 
#     'v': ['z', 'w']
# }
# print(adjancy_list(edges))