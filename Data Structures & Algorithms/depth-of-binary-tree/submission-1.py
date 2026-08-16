# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node)->int:
            '''
            returns the depth at node
            '''
            if not node:
                return 0
            depth = max(dfs(node.left), dfs(node.right)) + 1
            return depth
        return dfs(root)

