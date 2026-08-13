from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        # buckets map from count->Queue of recently used within that count
        self.buckets = defaultdict(OrderedDict)

        # key -> val
        self.value_lookup = {}
        # key -> count
        self.count_lookup = {}

        self.smallest_count = 1

    def get(self, key: int) -> int:
        '''
        - value not in cache: -1
        - value in cache:
            increment_item_count()
            return value
        '''

        if key not in self.value_lookup:
            return -1
        
        value = self.value_lookup[key]
        self.increment_item_count(key)
        return value

    def put(self, key: int, value: int) -> None:
        '''
        - value not in cache:
            CHECK: is cache full?
                - drop LRU (from lookups and bucket)

            insert into buckets[1] at end
            add to lookups
            used ++
        - value in cache:
            update value
            increment_item_count()
        '''

        if key not in self.value_lookup:
            if self.used == self.capacity:
                self.drop_lfu()

            # insert new value
            self.value_lookup[key] = value 
            self.count_lookup[key] = 1
            bucket = self.buckets[1]
            bucket[key] = None

            self.smallest_count = 1

            self.used +=1
        else:
            self.value_lookup[key] = value
            self.increment_item_count(key)

    def increment_item_count(self, key):
        '''
        INVARIANT: the key exists in the lfu cache
        '''

        # remove from existing bucket
        count = self.count_lookup[key]
        bucket = self.buckets[count]
        bucket.pop(key)

        # add to bucket at count + 1
        new_count = count + 1
        self.count_lookup[key] = new_count
        new_bucket = self.buckets[new_count]
        new_bucket[key] = None

        if count == self.smallest_count and len(self.buckets[count]) == 0:
            self.smallest_count = new_count

    def drop_lfu(self):
        '''
        INVARIANT: lfu cannot be empty
        '''
        assert self.used > 0

        bucket_at_smallest_count = self.buckets[self.smallest_count]
        key, _ = bucket_at_smallest_count.popitem(last=False)
        del self.value_lookup[key]
        del self.count_lookup[key]

        self.used -= 1

# we just keep track of the least frequently used element count (the lowest count)
# this is easy because: 
#  - if we evict the last item at that count its only because we're adding a new element which will be the NEW SMALLEST COUNT

# Reset the smallest_count to 1 when a new item is added
# When we "use" an item, check if count == smallest_count and if buckets[smallest_count] is empty. If so, update smallest_count += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)