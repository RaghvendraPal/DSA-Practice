graph_data = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

def Breadth_First_Search(source_data):

    data_queue = [source_data]
    result = []
    while data_queue:
        current_data = data_queue.pop(0)
        result.append(current_data)
        for value in graph_data[current_data]:
            data_queue.append(value)

    return result

print(Breadth_First_Search('a'))
