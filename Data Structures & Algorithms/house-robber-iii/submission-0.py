# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
decision based: if we rob the parent, we can't rob the child

greedy?
- simple checks like if the parent > both children succeed
- but what if the parent < both children - but > 1 child. Still possible to rob

dp:
- at each house make a decision: rob or not rob
- then our recursive call is to the children to produce the maximum amount of money we can get from that house GIVEN (we either can or can't rob it - based on the parent's decision)

why this is efficient - each node only has 2 possible computations that can be done on it:
1. max money from this house and down the tree if we CAN ROB IT
2. max money from this house and down the tree if we CAN'T ROB IT

cache these solutions: time complexity 2*n = O(2n)

'''

from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def maximumAmountOfMoneyFromThisHouseAndChildren(node: Optional[TreeNode], robbable: bool):
            # base case
            if not node:
                return 0
            
            # skip
            skip_money_from_left = maximumAmountOfMoneyFromThisHouseAndChildren(
                node.left, True
            )
            skip_money_from_right = maximumAmountOfMoneyFromThisHouseAndChildren(
                node.right, True
            )
            max_money_from_skipping = skip_money_from_left + skip_money_from_right
            if not robbable:
                # we early return the skip amount if its not robbable
                # so we don't compute the rob path when its result is not usable
                return max_money_from_skipping

            # rob
            rob_money_from_left = maximumAmountOfMoneyFromThisHouseAndChildren(
                node.left, False
            )
            rob_money_from_right = maximumAmountOfMoneyFromThisHouseAndChildren(
                node.right, False
            )
            max_money_from_robbing = node.val + rob_money_from_left + rob_money_from_right

            return max(max_money_from_skipping, max_money_from_robbing)

        return maximumAmountOfMoneyFromThisHouseAndChildren(root, True)



        