# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#         10
#     5       7
#  1     4  6    9

# at each node keep track of:
# - lower-bound for being valid - strict >
# - upper-bound for being valid - stright <
# if ANY node fails this check: we early return False

# what changes bounds:
# - going down the left subtree changes the UPPER bound
# - going down the right subtree changes the LOWER bound

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBstWithinBounds(node: Optional[TreeNode], lowerBound: int, upperBound: int):
            if not node:
                return True
            
            if not (node.val > lowerBound and node.val < upperBound):
                return False
            
            valid_left = validBstWithinBounds(node.left, lowerBound, node.val)
            valid_right = validBstWithinBounds(node.right, node.val, upperBound)

            return valid_left and valid_right

        return validBstWithinBounds(root, float('-inf'), float('inf'))
