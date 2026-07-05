class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # {0,3,2,5,4,6,1,1}
        # max seq: 0
        # current seq: 7
        # visited {0, 1, 2, 3, 4, 5, 6}

        # initialize a hash set with nums
        # initalize max seq 

        # for each num:
        #   check if its in visited - if so, skip

        #   initialize current seq = 1
        #   add item to visited
        #   while the next item exists in nums:
        #      add it to visited
        #       increment seq
        #   update max seq

        nums_set = set(nums)
        visited = set()
        max_seq = 0

        for num in nums_set:
            if num in visited:
                continue
            
            seq = 0
            seq_item = num
            while seq_item in nums_set:
                visited.add(seq_item)
                seq += 1
                seq_item+= 1
            max_seq = max(max_seq, seq)

        return max_seq
