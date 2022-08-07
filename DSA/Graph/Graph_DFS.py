def DFS_stack(source_node):
    graph_stack = []
    graph_stack.append(source_node)
    result = []
    while graph_stack:
        current_val = graph_stack.pop()
        result.append(current_val)
        for val in graph_data[current_val]:
            graph_stack.append(val)

    return result

graph_data = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

def DFS_recurr(node_val):
    if not graph_data[node_val]:
        return [node_val]
    
    result = []
    result.append(node_val)
    for val in graph_data[node_val]:
        v = DFS_recurr(val)
        if v:
            result.extend(v)
        

    return result

print(DFS_stack('a'))
print(DFS_recurr('a')) 