class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# We can not implement recursive version of queue

def tree_sum(root):
  if not root:
    return 0

  left_value = tree_sum(root.left)
  
  right_value = tree_sum(root.right)
  print(root.val, left_value, right_value)
  return root.val + left_value + right_value

def tree_sum_2(root):
  if not root:
    return 0

  return root.val + tree_sum_2(root.left) + tree_sum_2(root.right)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)        
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
print(tree_sum(a))
print(time.time() - time1)
time1 = time.time()
print(tree_sum_2(a))
print(time.time() - time1)
