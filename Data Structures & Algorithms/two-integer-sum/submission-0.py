class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_complete = {}
        for i, n in enumerate(nums):
            completed = to_complete.get(n, None)
            if completed is not None:
                return [completed, i]

            needed = target - n
            to_complete[needed] = i

            
                
