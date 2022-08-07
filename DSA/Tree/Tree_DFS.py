class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values(root):
  if not root:
    return []
  leftvalues = depth_first_values(root.left)
  rightvalues = depth_first_values(root.right)
  
  
  x = [root.val]
  x.extend(leftvalues)
  x.extend(rightvalues)
  # print(x)
  return x
#   leftvalues.extend(root.val)
#   leftvalues.extend(rightvalues)
#   return leftvalues

  # rightvalues.extend(root.val)
  # rightvalues.extend(leftvalues)
  # return rightvalues

def depth_first_values_stack(root):
  result = []
  stack = []
  stack.append(root)
  
  while stack:
    current_val = stack.pop(-1)
    if current_val:
      result.append(current_val.val)
      if current_val.right:
        stack.append(current_val.right)
      if current_val.left:
        stack.append(current_val.left)

  
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

print(depth_first_values(a))
print(depth_first_values_stack(a))