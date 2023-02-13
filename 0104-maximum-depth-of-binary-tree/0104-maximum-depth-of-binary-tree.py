# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDeep = 0
        if not root:
            return 0
        if (root.left or root.right):
            # print("node has children")
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            # print("last node")
            return 1
        
        #recursively search each side, returning the max depth of that side
        
        
        