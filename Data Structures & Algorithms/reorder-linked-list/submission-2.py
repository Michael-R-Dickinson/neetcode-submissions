# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        - find the middle of the list
        - reverse the second half of the list
        - now its easy to walk backwards through the second half (get n-1, n-2 etc.)
        
        merge by interleaving elements from the second list into the first
        """

        if head.next is None:
            return

        # find middle of list
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        middle = slow


        prev = middle.next
        curr = middle.next.next
        middle.next = None
        prev.next = None

        # reverse the second half
        if curr is not None:
            while curr is not None:
                temp = curr.next
                curr.next = prev

                prev = curr
                curr = temp               
        
        reversed_head = prev
        temp = reversed_head

        # interleave
        temp = head
        temp_rev = reversed_head
        while temp is not None and temp_rev is not None:
            next_original = temp.next
            next_rev = temp_rev.next

            temp.next = temp_rev
            temp_rev.next = next_original

            temp = next_original
            temp_rev = next_rev


        




