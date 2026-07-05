class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # walk the list backwards
        # for each index, figure out if it either, can jump to the last index, or if it can jump to an index which
        # has a path of jumps leading to the last index

        goalpost = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            max_target_idx = i + nums[i]
            if max_target_idx >= goalpost:
                goalpost = i
        
        return goalpost == 0