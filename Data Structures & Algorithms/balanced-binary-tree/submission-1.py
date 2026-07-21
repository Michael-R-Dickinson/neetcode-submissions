# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode)->int:
            """
            dfs down the tree and return height
            returns: height

            side effect: sets isBalances=False if |left.height - right.height| > 1
            """

            if not node:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1:
                return float('-inf')

            return max(left_height, right_height) + 1

        balanced = dfs(root) != float('-inf')

        return balanced