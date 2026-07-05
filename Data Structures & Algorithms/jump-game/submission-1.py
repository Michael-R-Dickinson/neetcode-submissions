class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach_end = set()
        # walk the list backwards
        # for each index, figure out if it either, can jump to the last index, or if it can jump to an index which
        # has a path of jumps leading to the last index

        for i in range(len(nums) - 1, -1, -1):
            for jump_size in range(nums[i] + 1):
                target_idx = i + jump_size
                if target_idx == len(nums) - 1 or target_idx in can_reach_end:
                    can_reach_end.add(i)
        
        return 0 in can_reach_end

                    