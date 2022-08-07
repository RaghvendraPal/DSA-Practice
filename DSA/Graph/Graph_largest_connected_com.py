def largest_component(graph):
    count = 0
    for node in graph:
        count_re = 0
        visited = []
        count_re = explore(graph, node, visited, count_re)
        if count < count_re:
            count = count_re

    print("Largest Count",count)
    return count

def explore(graph, node, visited = None, count_re = 0, memo= None):
    if not memo:
        memo = {}
    if visited is None:
        visited = []
    if node in visited:
        return 0
    if node in memo:
        return memo[node]

    visited.append(node)
    count_re = 1
    # print(graph[node])
    for val in graph[node]:
        count_re += explore(graph, val, visited)

    memo[node] = count_re

    # print(node, count_re)
    # print(memo)

    
    return memo[node]


print(explore({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}, 1))

print(explore({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}, 0))
largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4

largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6

largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 5

largest_component({}) # -> 0

largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 3