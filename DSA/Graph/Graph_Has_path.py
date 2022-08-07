# has path
# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two 
# nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the 
# source and destination nodes.

# Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, 
# not stubborn. -AZ

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
# def has_path(graph, source, destination):
#     if source == destination:
#         return True

#     for val in graph[source]:
#         if has_path(graph, val, destination):
#             return True

#     return False

def has_path(graph, source, destination):

    data_queue = [source]
    while data_queue:
        current_data = data_queue.pop(0)
        if current_data == destination:
            return True
        for value in graph[current_data]:
            data_queue.append(value)

    return False
print(has_path(graph, 'f', 'k')) # True

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'j')) # False

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'i', 'h')) # True

graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path(graph, 'v', 'w')) # True

graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path(graph, 'v', 'z')) # False