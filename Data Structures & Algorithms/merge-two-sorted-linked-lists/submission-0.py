# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        traverse both lists, adding them to a merged list
        add elements from the head of each list, based on which has a bigger VALUE

        end: if one list runs out, use the remaining list for the remaining elements
        """
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        temp1, temp2 = list1, list2
        dummy = ListNode()
        tail = dummy
        # invariants:
        #   tail - tail terminated
        #   temp1, temp2
        while temp1 is not None and temp2 is not None:
            if temp1.val < temp2.val:
                tail.next = temp1
                temp1 = temp1.next
            else:
                tail.next = temp2
                temp2 = temp2.next
            tail = tail.next
            tail.next = None

        if temp1 is None:
            tail.next = temp2
        else:
            tail.next = temp1

        res = dummy.next
        del dummy
        return res