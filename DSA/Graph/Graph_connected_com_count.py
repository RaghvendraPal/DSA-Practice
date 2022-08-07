# connected components count
# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
# The function should return the number of connected components within the graph.


# def connected_components_count(graph):
#     nodes = graph.keys()
#     visited_node = []
#     count = 0
#     for curr_node in nodes:
#         # print("Curr_node : ", curr_node)
#         # print("visited_node : ", visited_node)
#         queue_data = [curr_node]
#         flag = False
#         while queue_data:
#             current_node = queue_data.pop(0)
#             if not current_node in visited_node:
#                 flag = True
#                 visited_node.append(current_node)
#                 # print("visited_node : ", visited_node)
#                 for val in graph[current_node]:
#                     queue_data.append(val)
#         if flag:
#             count += 1

#     print("Total No. of Graphs: ",count)

def connected_components_count(graph):
    count = 0
    visited = []
    for node in graph:
        if explore(graph, node, visited):
            count += 1

    print("Total No.of Graphs : ",count)
    return count

def explore(graph, node, visited = []):
    if node in visited:
        return False

    visited.append(node)
    for val in graph[node]:
        explore(graph, val, visited)

    return True

connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2

connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 1

connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 3

connected_components_count({}) # -> 0

connected_components_count({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) # -> 5