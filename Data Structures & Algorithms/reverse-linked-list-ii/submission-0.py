# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
keep a dummy pointer to help with initialization
hold prev, curr -> iterate until we find the left node (left - 1 iterations puts curr at the node)
- prev stores the index to link to the current 'end'

use curr, next pointers to store the nodes we reverse the connection between
compute the number of iterations to reverse: right - left
- reverse that many connections
- next lands on the pointer we must link to the original first
'''

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        before_reverse = dummy
        for i in range(left-1):
            before_reverse=before_reverse.next
        
        # the nodes we'll reverse the connection between
        curr, next = before_reverse.next, before_reverse.next.next
        for i in range(right-left):
            temp = next.next
            next.next = curr
            curr = next
            next = temp

        after_reverse = next
        # last is the last node after reversing - should be pointed at after_reverse
        last = before_reverse.next
        last.next = after_reverse

        # point before_reverse at the new first
        before_reverse.next = curr

        return dummy.next
