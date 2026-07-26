# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
does node have any children:
- just one child: hoist that one
- 2 children: pick right child to hoist

2 children hoisting:
connect right as root:
- connect right child to parent.child
- connect left child to right.left

handle the old right.left - the stranded child of the node we hoisted
- walk the left subtree taking the 'right' path each time until we reach the bottom. Insert the right.left subtree there
'''

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs_for_node(node: Optional[TreeNode], target: int, parent: Optional[TreeNode]) -> Optional[TreeNode]:
            '''
            traverse the tree checking if the current node is the target. If it is, return the parent of the target node
            '''

            if node is None:
                return None, None
            if node.val == target:
                return node, parent

            left_result = dfs_for_node(node.left, target, node)
            right_result = dfs_for_node(node.right, target, node)

            return left_result if left_result[0] else right_result
        
    
        target, parent = dfs_for_node(root, key, None)
        # node isn't in tree
        if not target:
            return root

        new_node = None
        if not target.left and not target.right:
            # no children
            new_node = None
        elif target.left and target.right:
            # 2 children
            right = target.right
            left = target.left

            temp = right.left
            right.left = left
            
            # traverse down the left subtree to find a spot to insert the original left subtree of the node we're lifting
            # then add it as the rightmost component on that subtree
            left_subtree_curr = left
            while left_subtree_curr.right:
                left_subtree_curr = left_subtree_curr.right
            left_subtree_curr.right = temp

            new_node = right
        elif target.left:
            # only left child
            new_node = target.left
        elif target.right:
            # only right child
            new_node = target.right


        # insert the lifted node as the child of the original parent
        if not parent:
            # replacing the root node
            del target
            return new_node
        if target is parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
        del target
        return root

        




