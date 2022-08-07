class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def create(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            self._create(data, self.head)

    def _create(self, data, next):

        if next.data > data:
            if next.left == None:
                next.left = Node(data)
            else:
                self._create(data, next.left)

        elif next.data <= data:
            if next.right == None:
                next.right = Node(data)
            else:
                self._create(data, next.right)

    def traversal(self, type):
        if type == "in":
            self.inorder(self.head)
        elif type == "pre":
            self.preorder(self.head)
        elif type == "post":
            self.postorder(self.head)


    def inorder(self, head):
        if head == None:
            return
        else:
            self.inorder(head.left)
            print(head.data)
            self.inorder(head.right)
    
    def preorder(self, head):
        if head == None:
            return
        else:
            print(head.data)
            self.preorder(head.left)
            self.preorder(head.right)
    
    def postorder(self, head):
        if head == None:
            return
        else:
            self.postorder(head.left)
            self.postorder(head.right)
            print(head.data)

    def binary_search_tree_check(self, head):
        print("Data : ", head.data)
        if head.left:
            print("Data : ", head.data, "Left Value : ",head.left.data)
            if head.data > head.left.data:
                return self.binary_search_tree_check(head.left)
            elif head.data < head.left.data:
                print("Inside Left Else")
                return False
        elif head.right:
            print("Data : ", head.data, "Right Value : ",head.right.data)
            if head.data < head.right.data:
                return self.binary_search_tree_check(head.right)
            elif head.data > head.right.data:
                print("Inside Right Else")
                return False

        return True


tree = Tree()
list1 = [12, 36, 1, 4, 10, 3]
for val in list1:
    tree.create(val)

print("*"*20)
print("Inorder")
print("*"*20)
tree.traversal("in")
print("*"*20)
print("Preorder")
print("*"*20)
tree.traversal("pre")
print("*"*20)
print("Postorder")
print("*"*20)
tree.traversal("post")

tree1 = Node(10)
tree1.left = Node(9)
tree1.right = Node(11)
tree1.left.left = Node(8)
tree1.left.right = Node(12)
tree1.right.left = Node(1)
tree1.right.right = Node(1)

print("*"*10)
print(tree.binary_search_tree_check(tree1))
        