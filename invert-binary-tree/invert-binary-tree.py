

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            return self.invert(root)
        return root

    def invert(self, root: TreeNode) -> TreeNode:

        if root.right or root.left:

            root.right, root.left = root.left, root.right
            if root.left:
                self.invert(root.left)
            if root.right:
                self.invert(root.right)
            return root
        else:
            return root
        
        
        
