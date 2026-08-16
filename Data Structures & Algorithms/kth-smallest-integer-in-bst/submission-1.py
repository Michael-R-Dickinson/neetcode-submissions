# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we need: inorder traversal AND add to a count until we reach k
# HOWEVER, we should return early once we reach k nodes so we dont traverse the entire rest of the tree

# before adding the current node in the dfs to the list of k_smallest, we check the current size of k_smallest
# - if its already full up to k, we dont add it AND we dont traverse the right subtree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen_so_far = 0
        def inorder_traversal(node: Optional[TreeNode])->int:
            '''
            performs inorder traversal. First recurses on the left subtree. 
            if the left subtree found the kth smallest, returns that


            Then checks if seen_so_far == k - 1
            - if so, then this node is the kth smallest -> returns that node.val
            - increments the seen_so_far counter

            then recurses on the right subtree and returns its result
            '''
            nonlocal seen_so_far


            if not node:
                return None

            left_result = inorder_traversal(node.left)
            if left_result: return left_result
            if seen_so_far == k - 1:
                return node.val
            seen_so_far += 1

            right_result = inorder_traversal(node.right)
            return right_result
        return inorder_traversal(root)
            
