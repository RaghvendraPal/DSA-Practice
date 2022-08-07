# Python3 program to correct the BST
# if two nodes are swapped
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		
		self.key = data
		self.left = None
		self.right = None

# Utility function to track the nodes
# that we have to swap
def correctBstUtil(root, first, middle,
				last, prev):
						
	if(root):
		
		# Recur for the left sub tree
		correctBstUtil(root.left, first,
					middle, last, prev)
						
		# If this is the first violation, mark these
		# two nodes as 'first and 'middle'
		if(prev[0] and root.key < prev[0].key):
			if(not first[0]):
				first[0] = prev[0]
				middle[0] = root
			else:
				
				# If this is the second violation,
				# mark this node as last
				last[0] = root
				
		prev[0] = root
		
		# Recur for the right subtree
		correctBstUtil(root.right, first,
					middle, last, prev)
	
# A function to fix a given BST where
# two nodes are swapped. This function
# uses correctBSTUtil() to find out two
# nodes and swaps the nodes to fix the BST
def correctBst(root):
	
	# Followed four lines just for forming
	# an array with only index 0 filled
	# with None and we will update it accordingly.
	# we made it null so that we can fill
	# node data in them.
	first = [None]
	middle = [None]
	last = [None]
	prev = [None]
	
	# Setting arrays (having zero index only)
	# for capturing the required node
	correctBstUtil(root, first, middle,
				last, prev)

	# Fixing the two nodes
	if(first[0] and last[0]):
		
		# Swapping for first and last key values
		first[0].key, last[0].key = (last[0].key,
									first[0].key)

	elif(first[0] and middle[0]):
	
		# Swapping for first and middle key values
		first[0].key, middle[0].key = (middle[0].key,
										first[0].key)
	
	# else tree will be fine

# Function to print inorder
# traversal of tree
def PrintInorder(root):
	
	if(root):
		PrintInorder(root.left)
		print(root.key, end = " ")
		PrintInorder(root.right)
		
	else:
		return

# Driver code

#	 6
#	 / \
# 10 2
# / \ / \
# 1 3 7 12

# Following 7 lines are for tree formation
root = Node(6)
root.left = Node(10)
root.right = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(7)
root.right.right = Node(12)

# Printing inorder traversal of normal tree
print("inorder traversal of normal tree")
PrintInorder(root)
print("")

# Function call to do the task
correctBst(root)

# Printing inorder for corrected Bst tree
print("")
print("inorder for corrected BST")

PrintInorder(root)

# This code is contributed by rajutkarshai


 

# We can not implement recursive version of queue


a = Node(3)
b = Node(2)
c = Node(5)
d = Node(1)
e = Node(4)
f = Node(6)        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print("inorder traversal of normal tree")
PrintInorder(a)
print("")

# Function call to do the task
correctBst(a)

# Printing inorder for corrected Bst tree
print("")
print("inorder for corrected BST")

PrintInorder(a)



#      a                    4
#    /   \                /   \         
#   b     c              2     5   
#  / \     \            / \     \ 
# d   e     f          1   3     6
