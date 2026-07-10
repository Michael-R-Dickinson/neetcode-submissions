"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Naive:
deep copy the linked list without the random pointers set
- then iterate over the linked list and for each node - walk the linked list until the node random points to is found - make the assignment
O(n^2) - not too good

O(n) memory:
- create a list of pointers to each node
- deep copy the linked list with random set to null - and add entries in the list
- walk our linked list and assign random to the correct nodes using the pointers from the list

O(n) time
O(n) space

Pseudo code:
for each entry in linked list:
    - create a copy of the node - without random set
    - store node in node_index[idx]
    - use a dummy node to help link up the 'next' pointers

for each entry in linked list (and corresponding deepcopy):
    - lookup pointer to 'random' node in node_idex
    - set 'random' to this node
"""



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_index = []
        node_to_index = {}

        dummy = Node(0)

        curr_copy = dummy
        curr_original = head
        while curr_original:
            new = Node(curr_original.val)
            node_index.append(new)
            curr_copy.next = new

            cur_idx = len(node_index) - 1
            node_to_index[id(curr_original)] = cur_idx

            curr_copy = curr_copy.next
            curr_original = curr_original.next
        
        curr_copy = dummy.next
        curr_original = head
        while curr_original:
            if curr_original.random != None:
                random_idx = node_to_index[id(curr_original.random)]
                curr_copy.random = node_index[random_idx]

            curr_copy = curr_copy.next
            curr_original = curr_original.next

        return dummy.next
            

