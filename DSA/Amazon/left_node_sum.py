class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def isLeaf(node):
    if (node.left == None) and (node.right == None):
        return True
    return False

def leftNodeSum(tree):
    sum = 0
    if tree.left:
        value = leftNodeSum(tree.left)
        sum = tree.left.data + value
    if tree.right:
        sum += leftNodeSum(tree.right)

    return sum

def leaf_sum(tree):
    sum = 0
    if isLeaf(tree):
        sum += tree.data
    if tree.left:
        sum += leaf_sum(tree.left)

    if tree.right:
        sum += leaf_sum(tree.right)

    return sum








tree = Node(2)
tree.left = Node(3)
tree.right = Node(1)
tree.left.left = Node(-1)
tree.left.right = Node(4)
tree.right.left = Node(-2)
tree.right.right = Node(7)
print(leftNodeSum(tree))
print(leaf_sum(tree))

#             23
    
#     10              20

# 15      0       11      13
