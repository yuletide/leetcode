# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import json

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # start with root node, do DFS and serialize children, returning back up the tree, compare final lists
        # python list equality works for this
        if not p and not q:
            return True

        if not p or not q:
            return False

        # serialize tree to list recursively, with accumulator (like reduce())
        aTree = self.dfs(p, [])
        bTree = self.dfs(q, [])
        # print(aTree, bTree)
        # json.dumps(aTree)
        return aTree == bTree
        
    def dfs(self, node, acc):
        # if leaf node
        if not node:
            return acc
        if not node.left and not node.right:
            # print("leaf", node.val)
            acc.append(node.val)
            return acc
        acc.append(node.val)
        if node.left:
            self.dfs(node.left, acc)
        else:
            acc.append(None)
        if node.right: # dont append a null for missing right nodes, per example
            self.dfs(node.right, acc)
        # else:
            # acc.append(None)
        return acc



        