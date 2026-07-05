class ListNode:
    def __init__(self, value, next, min):
        self.value = value
        self.next = next
        self.min = min

class MinStack:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val: int) -> None:
        node = ListNode(val, None, -1)
        if (self.head == None):
            self.head = node
            self.tail = node
            node.min = val
        else:
            node.min = val if val < self.head.min else self.head.min
            node.next = self.head
            self.head = node
            

    def pop(self) -> None:
        if self.head == None:
            return
        temp = self.head
        self.head = self.head.next
        del temp

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.min
