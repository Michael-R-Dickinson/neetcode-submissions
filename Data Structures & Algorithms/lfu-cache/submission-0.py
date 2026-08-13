 
'''
Heap?
- insert log(n)
- remove log(n)
- PUT requires us to increment the use_counter for a value in the heap -> REMOVE + INSERT operations - O(log(n)) - not usable

Linked List: [BIG]->[SMALL], [USED MORE RECENTLY]->[USED LESS RECENTLY]
- find linked list element: O(1)
- move linked list element: O(n)

use order: 1,2,3,1,2

list: [1 2]
freq: [1 1]
O(n) average time :(
'''

'''
least frequently used is DROPPED on a PUT operation
- tiebreaker -> least recently used

'use counter':
- starts at 1
- incremented on GET or PUT

need:
- O(1) way to get the value/values with the lowest use counter?

use_counter: something ordered thats easily reorderable

Doubly Linked List + Hashmap:
- hashmap keeps references to items in linked list -> quickly find and increment use_count
    - reorder by moving it down the linked list until we find a value >= it

Frequency Buckets?
buckets: [LESS FREQUENT... MORE FREQUENT]
within bucket: [LESS RECENT... MORE RECENT]

use order: 1,2,3,1,2
list: [[3], [1, 2]]
freq: [1, 2]

each use:
- gauranteed to remove the element from the bucket: O(1)
- gauranteed to place it at the end of the next bucket: O(1) - its always the most recently used

invalidate + remove least frequently used:
- simply the first element in the first bucket

How do we store the buckets?
- list: easy to get the next bucket
    if each node stores its use_count on it, then we simply do buckets[use_count+1]
    BUT: list size = max(use_counts) - one element but we use it 10000 times - 10000 sized array for one item
- linked list: harder to get the next bucket
    we need to have our node lookup hold a reference to the BUCKET and the NODE 
    BUT: num_buckets = count(unique use_counts)

stick with a list for now.

Implementation:
Initialize:
- buckets: empty array
- lookup: empty dict[key: ListNode]
- capacity
- used count

Get:
- check lookup for key -> return node.val or -1
- increment_element_usage(node)

Put:
- check lookup for key
    - found: dont update used_count, increment_element_usage(node), update value
    - not found: update used_count, add new element to frequency_buckets[1]

increment_element_usage(node):
- remove element from bucket, add to next bucket, update node.frequency

a few implict things:
initializing buckets:
- we check if use_count >= len(freq_buckets)
    -> init bucket: head and tail sentinels
'''

class ListNode:
    def __init__(self, key, val, frequency, prev=None, next=None):
        self.key = key
        self.val = val
        self.frequency = frequency
        self.prev = prev
        self.next = next
    
class DoublyLinkedList:
    def __init__(self):
        self.head_sentinel = ListNode(None, None, None)
        self.tail_sentinel = ListNode(None, None, None)
        self.head_sentinel.next = self.tail_sentinel
        self.tail_sentinel.prev = self.head_sentinel
    
    def insert_at_tail(self, node):
        target = self.tail_sentinel.prev
        DoublyLinkedList.insert_after(target, node)

    def drop_at_head(self):
        assert not self.empty
        head = self.head
        DoublyLinkedList.remove_list_node(head)
        return head
    
    @property
    def head(self):
        if self.empty:
            return None
        return self.head_sentinel.next

    @property
    def tail(self):
        if self.empty:
            return None
        return self.tail_sentinel.prev
    
    @property
    def empty(self):
        return self.head_sentinel.next == self.tail_sentinel
    
    @staticmethod
    def insert_after(target, node):
        prev = target
        next = target.next

        prev.next = node
        node.prev = prev

        next.prev = node
        node.next = next

    @staticmethod
    def remove_list_node(node):
        '''
        INVARIANT: node must not be the head or tail of the LL
        '''
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

class LFUCache:

    def __init__(self, capacity: int):
        # frequency 0 is never populated as anything in the cache has been used at minimum once
        # frequency 1 is initialized to make it easy to insert new element (which always have freq=1) into the buckets
        self.freq_buckets = [DoublyLinkedList(), DoublyLinkedList()]
        self.lookup = {}
        self.capacity = capacity
        self.used = 0

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]
        self.increment_element_usage(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.increment_element_usage(node)
        else:
            if self.used == self.capacity:
                self.drop_lfu()

            new = ListNode(key, value, 1)
            self.freq_buckets[1].insert_at_tail(new)
            self.lookup[key] = new
            self.used += 1

    def increment_element_usage(self, node: ListNode):
        DoublyLinkedList.remove_list_node(node)
        node.frequency += 1
        if node.frequency >= len(self.freq_buckets):
            # init new bucket
            bucket = DoublyLinkedList()
            self.freq_buckets.append(bucket)
        else:
            bucket = self.freq_buckets[node.frequency]

        bucket.insert_at_tail(node)

    def drop_lfu(self):
        # assumes theres atleast one nonempty bucket
        for i, bucket in enumerate(self.freq_buckets):
            if not bucket.empty:
                break

        dropped = bucket.drop_at_head()
        del self.lookup[dropped.key]

        self.used -= 1
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)