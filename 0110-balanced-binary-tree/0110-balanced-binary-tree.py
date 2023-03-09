# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced: a tree where depth of two subtrees of every node never differs by more than one
        # we will do DFS and return two values (or overload with -1 as unbalanced)

        # output: true / false
        # traversal will be recursive
        # steps: for a given node, it is balanced if the subtree depth of its child nodes dont differ more than one and none of the subtrees are unbalanced
        return self.depth(root)[1]

    def depth(self, node):
        # search a node subtree and return depth and also check if we are balanced at this subtree level
        # to avoid lots of checks, just return depth of 0 if null
        if not node:
            return 0, True
        # print('node', node.val)
        
        # check if leaf node
        if not node.left and not node.right:
            # leaf node
            # print('leaf')
            return 1, True
        
        # if this subtree is unbalanced, return -1
        lDepth = self.depth(node.left)
        rDepth = self.depth(node.right)
        # print(lDepth, rDepth, abs(lDepth[0] - rDepth[0]) < 2)
        depth = max(lDepth[0], rDepth[0]) + 1
        balanced = lDepth[1] and rDepth[1] and abs(lDepth[0] - rDepth[0]) < 2
        return depth, balanced

        
