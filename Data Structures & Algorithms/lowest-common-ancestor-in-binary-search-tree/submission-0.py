# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        searching for a node with:
        p.val <= node.val <= q.val 
        or
        q.val <= node.val <= p.val

        Begin by appyling DFS for p
        At each step check if our condition is satisifed
        """


        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)




