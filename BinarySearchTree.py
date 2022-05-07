class Node:
    def __init__(self, data):
        self.front = None
        self.data = data
        self.rear = None

class Tree:
    def __init__(self):
        self.head = None

    def create(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            self.create1(node, data, self.head)



    def create1(self, node, data, next):

        if next.front == None and next.rear == None:
            if next.data <= data:
                next.front = node
            else:
                next.rear = node
            return
        elif next.data <= data:
            self.create1(node, data, next.front)
        elif next.data > data:
            self.create1(node, data, next.rear)

    def traverse(self, next):
        if next.front == None:
            print(next.data)
            return
        else:
            self.traverse(next.front)
            self.traverse(next.rear)


tree = Tree()
tree.create(19)
tree.create(20)
tree.create(10)
tree.create(11)

tree.traverse()





        