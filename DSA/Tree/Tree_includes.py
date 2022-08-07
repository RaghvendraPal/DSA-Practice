class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# We can not implement recursive version of queue

def tree_includes(root, target):
  bool_value = False
  if not root:
    return bool_value
  
  if root.val == target:
    bool_value = True
    return bool_value
  bool_value = tree_includes(root.left, target)
  if not bool_value:
    bool_value = tree_includes(root.right, target)
  
  return bool_value

def tree_includes_2(root, target):
  if not root:
    return False
  
  if root.val == target:
    return True
  return tree_includes(root.left, target) or tree_includes(root.right, target)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
import time
time1 = time.time()
print(tree_includes(a, 'g'))
print(time.time() - time1)
time1 = time.time()
print(tree_includes_2(a, 'g'))
print(time.time() - time1)
