graph = {
    'a':['c', 'b'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

class Breadth:

    def breadthfirststack(self, source):
        tail = len(graph.keys())
        queue = [ source ]
        index = 0
        while (index < tail):
            current_node = queue[index]
            print(current_node, end = '->')
            for val in graph[current_node]:
                queue.append(val)
            index += 1
        
    def breadthfirstrecursion(self, source):
        print(source)
        for val in graph[source]:
            self.breadthfirstrecursion(val)


d = Breadth()
d.breadthfirststack('a')
print("*"*100)
d.breadthfirstrecursion('a')

