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
        self.queue_front_sentinel = ListNode()
        self.queue_back = self.queue_front_sentinel
        self.capacity = capacity
        self.used = 0
        # back are new entries or recently used
        # front are old entries about to be dropped from the cache

        # queue is empty when queue_front == queue_back
        # the actual front of the queue is queue_front_sentinel.next

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
        self.queue_back.next = new
        new.prev = self.queue_back
        self.queue_back = new

        self.lookup[key] = new

        self.used += 1

    def drop_least_recently_used(self):
        self.used -= 1
        least_recently_used = self.queue_front_sentinel.next

        del self.lookup[least_recently_used.key]

        # if capacity=1, then this item is both the front and back of the queue
        # so if we drop it, we must update the self.queue_back
        if self.capacity == 1:
            self.queue_back = self.queue_front_sentinel
            return
        
        # remove from queue
        next = least_recently_used.next
        prev = self.queue_front_sentinel

        next.prev = prev
        prev.next = next

    def move_to_back(self, item: ListNode):
        # if item is the front of the list -> normal removal is fine
        # if item is back of the list -> already the most recently used so we don't need to move it at all
        if item == self.queue_back:
            return

        prev = item.prev
        next = item.next
        
        # connect prev and next to eachother
        prev.next = next
        next.prev = prev
    
        # replace at back of queue
        self.queue_back.next = item
        item.prev = self.queue_back
        item.next = None
        self.queue_back = item
