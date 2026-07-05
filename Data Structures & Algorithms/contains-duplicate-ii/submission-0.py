class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(k + 1):
            if i >= len(nums):
                break
            if nums[i] in window:
                return True
            window.add(nums[i])

        print(window)
        l, r = 0, k
        while r < len(nums) - 1:
            # move the window
            window.remove(nums[l])
            l += 1
            r += 1
            if nums[r] in window:
                return True
            window.add(nums[r])

        return False
        

