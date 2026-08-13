# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
overflow from one figure adds to the next in the list

Edge cases:
- One list is shorter than another: we effectively pad the shorter one with zeros

solution:
- traverse both lists in tandem
- keep track of: carry amount added to the next digit, current pointer in both lists, current pointer in new list

At each step:
- create a new ListNode with the value at that figure
- add it to the tail of the new list

'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        dummy = ListNode()

        curr = dummy
        
        while l1 or l2 or carry:
            # calculate the total value at this figure including carry
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val
            if carry:
                val += 1
                carry = False
            
            # determine if we overflowed at this figure, and add it to the next digit's carry
            if val >= 10:
                val -= 10
                carry = True

            new = ListNode(val)
            curr.next = new
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next





        
        