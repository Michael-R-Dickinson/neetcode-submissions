# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# just checking if 2 trees are the same BUT we wait to start checking until we find a node in the 'root' tree with the value of the root in the subtree. 
# One note: if we find the subroots value, we check the subtree for equality. BUT we cant write it off just because.

# to start: lets submit a solution where we just search for val, then check for exact equality

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSubrootEquality(subroot1, subroot2):
            if not subroot1 and not subroot2:
                return True
            if not subroot1 or not subroot2:
                return False
            if not subroot1.val == subroot2.val:
                return False
            
            left_result = checkSubrootEquality(subroot1.left, subroot2.left)
            right_result = checkSubrootEquality(subroot1.right, subroot2.right)

            return left_result and right_result

        def findSubroots(node: Optional[TreeNode])-> bool:
            if not node:
                return False
                
            current_search = checkSubrootEquality(node, subRoot)
            left_search = findSubroots(node.left) 
            right_search = findSubroots(node.right) 
            return left_search or right_search or current_search
        return findSubroots(root)

            