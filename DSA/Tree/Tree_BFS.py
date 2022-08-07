class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# We can not implement recursive version of queue

def breadth_first_values_queue(root):
  result = []
  queue= []
  queue.append(root)
  
  while queue:
    current_val = queue.pop(0)
    if current_val:
      result.append(current_val.val)
      if current_val.left:
        queue.append(current_val.left)
      if current_val.right:
        queue.append(current_val.right)
  
#   print(result)
  return result


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

print(breadth_first_values_queue(a))
