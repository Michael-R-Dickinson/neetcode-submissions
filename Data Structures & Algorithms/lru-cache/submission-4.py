from collections import deque

class ListNode:
    def __init__(self, key = None, val=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        # drop at head
        # insert at tail
        # queue front = linked list head
        self.q_front_sentinel = ListNode()
        self.q_back_sentinel = ListNode()
        self.q_front_sentinel.next = self.q_back_sentinel
        self.q_back_sentinel.prev = self.q_front_sentinel

        self.capacity = capacity
        self.used = 0
        # back are new entries or recently used
        # front are old entries about to be dropped from the cache

        # queue is empty when queue_front.next == queue_back
        # the actual front of the queue is q_front_sentinel.next
        # and actual back is q_back_sentinel.prev

        self.lookup = {}

    def get(self, key: int) -> int:
        # moves the item at key to the back of the queue
        item = self.lookup.get(key, None)
        if item is None:
            return -1

        self.move_to_back(item)
        return item.val


    def put(self, key: int, value: int) -> None:
        item = self.lookup.get(key, None)
        if item:
            # we just need to update its value, no movement in the cache
            item.val = value
            self.move_to_back(item)
            return
        
        if self.capacity == self.used:
            # we would go over capacity if we added this item
            self.drop_least_recently_used()


        new = ListNode(key, value)
        # Insert at back of queue
        target = self.q_back_sentinel.prev
        self.insert_after(target, new)

        self.lookup[key] = new

        self.used += 1

    def drop_least_recently_used(self):
        # Make sure we aren't trying to drop from an empty cache
        assert self.q_front_sentinel.next is not self.q_back_sentinel

        self.used -= 1
        least_recently_used = self.q_front_sentinel.next

        # remove from queue
        self.remove(least_recently_used)

        del self.lookup[least_recently_used.key]

    def move_to_back(self, item: ListNode):
        self.remove(item)
        self.insert_after(self.q_back_sentinel.prev, item)
        

    def remove(self, node: ListNode):
        """
        INVARIANT: node cannot be a sentinel
        """

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert_after(self, target: ListNode, node: ListNode):
        """
        inserts node after target in the queue
        INVARIANT: node cannot be a sentinel
        """

        prev = target
        next = target.next

        prev.next = node
        next.prev = node

        node.prev = prev
        node.next = next

