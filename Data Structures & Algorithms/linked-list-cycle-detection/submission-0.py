# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
fast and slow pointers
if fast ever catches up to slow -> we have a cycle

fast goes by 2 places at a time
slow by 1

if fast reaches the end of the list:
    - no cycle

if fast catches up to slow:
    - cycle

one is gauranteed to be reached

'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast = head.next
        slow = head
        
        while fast and fast.next:
            if fast is slow:
                return True
            fast = fast.next.next
            slow = slow.next 

        return False

