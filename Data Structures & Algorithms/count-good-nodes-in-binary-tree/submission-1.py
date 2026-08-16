# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# what we need to know at each node: the biggest number above it in the tree

# then at each node check: is the biggest number above it <= that nodes value -> increment the count


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGoodNodesInSubtree(node: Optional[TreeNode], greatestNodeAbove: int)->int:
            if not node:
                return 0
            
            newGreatestAbove = max(greatestNodeAbove, node.val)
            goodNodesInLeft = countGoodNodesInSubtree(node.left, newGreatestAbove)
            goodNodesInRight = countGoodNodesInSubtree(node.right, newGreatestAbove)

            goodNodesInChildren =  goodNodesInLeft + goodNodesInRight
            if greatestNodeAbove <= node.val:
                return goodNodesInChildren + 1
            return goodNodesInChildren

        return countGoodNodesInSubtree(root, float('-inf'))