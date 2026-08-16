# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            
            dfs(node.left)
            out.append(node.val)
            dfs(node.right)
        dfs(root)
        
        return out