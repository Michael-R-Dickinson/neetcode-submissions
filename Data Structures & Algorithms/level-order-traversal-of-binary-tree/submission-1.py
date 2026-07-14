# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Breadth first search
- maintain a queue of nodes
- for each node we traverse, add its children
- traverse nodes by dequeuing
- delinate levels by noting which node is farthest "left" at each level
    - when it adds its children - it marks its left child as the new farthest left
    - when a 'farthest left' node is reached, we start a new sublist


pseudo code:

init queue
init output 2d list

add first node to queue
mark it far_left

while queue:
    dequeue a child
    if it is marked far_left, create a new sublist and mark its left child far_left

    add children
    add node to current sublist in output
"""

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        queue = deque()
        queue.appendleft(root)
        nodes_in_level = 1
        nodes_traversed_in_level = 0

        out = [[]]
        while queue:
            if nodes_traversed_in_level == nodes_in_level:
                nodes_in_level = len(queue)
                nodes_traversed_in_level = 0
                out.append([])

            node = queue.pop()
            current_sublist = out[-1]
            current_sublist.append(node.val)

            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

            nodes_traversed_in_level += 1
        return out




