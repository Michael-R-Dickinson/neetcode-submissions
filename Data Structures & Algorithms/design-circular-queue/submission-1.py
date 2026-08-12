'''
allocate an array to store the queue
we need to keep track of: 
- queue_front: the front element of the queue
- queue_back: the index we will insert at next 


all indexing is handled % capacity
empty queue:
- queue_front == queue_back
full:
- queue_back == queue_front
SOLUTION: just keep track of capacity to disambiguate

front: q[queue_front]
back: q[queue_back - 1]

edge conditions:
- enqueue on full -> return False
- dequeue on empty -> return False
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.queue_front_idx = 0
        self.queue_back_idx = 0

        self.capacity = k
        self.used = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.queue_back_idx] = value
        self.queue_back_idx = (self.queue_back_idx + 1) % self.capacity
        self.used += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.q[self.queue_front_idx] = None
        self.queue_front_idx = (self.queue_front_idx + 1) % self.capacity
        self.used -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.queue_front_idx]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[(self.queue_back_idx - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.used == 0

    def isFull(self) -> bool:
        return self.capacity == self.used
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()