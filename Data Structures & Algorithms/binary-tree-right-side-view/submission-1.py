# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
some kind of level order traversal
and grab the rightmost element in the level order

level order traversal:
- queue
- track the length of each layer - when we finish a layer, the number of nodes in the queue is the number of nodes in the next layer
- once we traverse this many nodes, we know we're done with that layer

problem specifics: keep a list of the "last" node we travere in each layer (assuming we add nodes node.left -> node.right)
'''
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        right_side_view = []

        # level order traversal
        q = deque()
        remaining_in_layer = 1
        q.append(root)

        while q:
            curr = q.popleft()
            remaining_in_layer -= 1

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

            if remaining_in_layer == 0:
                right_side_view.append(curr.val)
                remaining_in_layer = len(q)

        return right_side_view
        