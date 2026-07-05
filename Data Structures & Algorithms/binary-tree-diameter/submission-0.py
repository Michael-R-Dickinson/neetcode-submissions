# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Idea:
        recurse down the tree, and find maximum depth of both subtrees
        add this together and this is the max distance of any two leaf nodes
        from each subtree

        We return both the height of the current node
        and the max distance

        then the parent takes the maximum value between the max distance calculation
        at its children nodes, and the max distance it calculates using their depth
        """
        
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            height = max(left_height, right_height) + 1

            res = max(res, left_height + right_height)

            return height

        dfs(root)
        return res

