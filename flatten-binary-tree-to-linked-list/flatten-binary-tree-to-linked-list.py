# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
    
        """
        def traverse(node: TreeNode):
            nonlocal head
            if node ==None:
                return
            right = node.right
            left = node.left
            node.left = None
            node.right = None
            
            if head:
                head.right = node
            head = node
            
            traverse(left)
            traverse(right)
            
        
        if root == None: return 0
        head = None
        traverse(root)
        