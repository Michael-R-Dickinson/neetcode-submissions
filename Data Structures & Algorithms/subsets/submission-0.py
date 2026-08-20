# nums = [ 1 2 3 4 5 ]
# 1 0 0 1 1
# subset = [ 1 4 5 ]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        for mask in range(1 << len(nums)):
            subset = [
                num for i, num in enumerate(nums) 
                    if ((1<<i) & mask) != 0
            ]
            power_set.append(subset)
        return power_set