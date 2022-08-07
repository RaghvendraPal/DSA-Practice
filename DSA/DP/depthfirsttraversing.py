graph = {
    'a':['b', 'c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

class Depth:

    def depthfirststack(self, source):
        stack = [ source ]
        while (len(stack) > 0):
            current_node = stack.pop()
            print(current_node)
            for val in graph[current_node]:
                stack.append(val)
        
    def depthfirstrecursion(self, source):
        print(source)
        for val in graph[source]:
            self.depthfirstrecursion(val)


d = Depth()
d.depthfirststack('a')
print("*"*100)
d.depthfirstrecursion('a')

