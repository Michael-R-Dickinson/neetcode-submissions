# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        walk n steps through the linked list
        keeping track of a prev (n-1), and curr (n)
        remove curr

        base cases:
        - no elements
        """
        if head is None or head.next is None:
            return None
        
        right = head
        length = 0
        while right is not None:
            right = right.next
            length += 1
        
        delete_idx = length - n
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        for i in range(0, delete_idx):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        del curr
        return dummy.next
        

            
        

        