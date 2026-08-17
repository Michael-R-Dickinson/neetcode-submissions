# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
take indexes into preorder and inorder:
SPLIT the inorder traversal by the first index in preorder

        10
    7       12
  1    8  11    14

inorder [ 1 7 8 10 11 12 14]
preorder [ 10 7 1 8 12 11 14 ]

inorder_split_idx = 3

inorder [1 7 8], [11 12 14]
preorder: [7 1 8], [12 11 14]

indexing - bot inclusive, top exclusive:
inorder: [bottom, split_idx], [split_idx + 1, top]
preorder: [bottom+1, bottom+1+len(inorder_left)] [bottom+1+len(inorder_left), top]
'''


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_idx_lookup = {num: idx for idx, num in enumerate(inorder)}


        def buildTreeFromTraversals(inorder_bot, inorder_top, preorder_bot, preorder_top)->Optional[TreeNode]:
            assert inorder_top - inorder_bot == preorder_top - preorder_bot

            if inorder_top-inorder_bot == 0:
                return None
            
            current = preorder[preorder_bot]
            inorder_split_idx = inorder_idx_lookup[current]

            node = TreeNode(current)

            # left
            left_subtree_len = inorder_split_idx - inorder_bot
            node.left = buildTreeFromTraversals(
                inorder_bot, inorder_split_idx,
                preorder_bot+1, preorder_bot+1+left_subtree_len
            )

            # right
            node.right = buildTreeFromTraversals(
                inorder_split_idx+1, inorder_top,
                preorder_bot+1+left_subtree_len, preorder_top
            )

            return node

        return buildTreeFromTraversals(0, len(inorder), 0, len(preorder))







