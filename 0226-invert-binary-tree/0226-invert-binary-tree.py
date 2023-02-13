# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        return self.invertNode(root)
    
    def invertNode(self, node: Optional[TreeNode]) -> TreeNode:
        l, r = node.left, node.right
        # newNode = TreeNode(val=node.val)
        # print(node)
        if l:
            node.right = self.invertNode(l)
        else:
            node.right = None
        
        if r:
            node.left = self.invertNode(r)
        else:
            node.left = None
        # print("inverted", node)
        return node


