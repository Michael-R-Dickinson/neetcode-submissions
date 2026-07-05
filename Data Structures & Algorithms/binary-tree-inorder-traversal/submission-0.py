# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        left_inorder = self.inorderTraversal(root.left)
        right_inorder = self.inorderTraversal(root.right)


        left_inorder.append(root.val)
        left_inorder.extend(right_inorder)
        return left_inorder