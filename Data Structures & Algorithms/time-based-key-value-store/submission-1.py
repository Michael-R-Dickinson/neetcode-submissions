class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # binarySearch returns the index where the first value higher than timestamp exists
        # could be == len(data) if no ts exists > timestamp
        # so if binarySearch() == len(data) we know data[-1] is the highest ts <=timestamp
        # if binarySearch() == 0, then all data > timestamp so we return ""

        def binarySearch(low, high, target, data):
            if high < low:
                return low

            mid = (low + high) // 2
            mid_ts, mid_val = data[mid]

            if mid_ts == target:
                return mid+1
            
            if mid_ts < target:
                return binarySearch(mid+1, high, target, data)
            else:
                return binarySearch(low, mid-1, target, data)
        
        data = self.m[key]
        idx_lte_timestamp = binarySearch(0, len(data)-1, timestamp, data)
        if not data:
            return ""
        if idx_lte_timestamp == 0:
            return ""
        ts, val = data[idx_lte_timestamp - 1]
        return val
        
# [1 2 4 6 9]
# timestamp = 3
# return 2 so low - 1
# what if timestamp = 0 -> return ""

        


