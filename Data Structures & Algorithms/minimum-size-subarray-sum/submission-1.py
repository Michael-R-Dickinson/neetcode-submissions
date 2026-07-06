# Sliding window
# move right pointer along
# move left pointer whenever its possible to satisfy 
# the target with fewer nums
# if window >= target: log length
# if window - nums[l] >= target: then drop nums[l] 
#   until removing another nums[l] would make the window < target
# 
# Idea: we grow until we have >= target in the window
# then shrink to as small as possible 

# loop invariant: window is always >= target 
#   (except during initilaization where it expands to be)

# structure
# for
#   add r to window
#   init handling: if window < target: continue
#   push l until the window would be invalid if we pushed it anymore
#       & log subarray len




class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_window = float('inf')
        l = 0
        for r in range(len(nums)):
            if sum(nums[l:r+1]) < target:
                continue

            min_window = min(min_window, r - l + 1)
            while sum(nums[l:r+1]) - nums[l] >= target:
                l += 1
                min_window = min(min_window, r - l + 1)
        if min_window == float('inf'):
            return 0
        return min_window


            