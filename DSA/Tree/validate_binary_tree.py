# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif (root.left != None) and (root.left.val >= root.val):
            return False
        elif (root.right != None) and (root.right.val <= root.val):
            return False
        elif (not self.isValidBST(root.left)) or (not self.isValidBST(root.right)):
            return False
        return True
        
