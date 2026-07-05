class Solution:
    def search_bounded(self, nums, target, bot, top):
        size = top - bot
        if size <= 0:
            return -1

        middle_idx = bot + (size // 2)
        middle_el = nums[middle_idx]
        if target == middle_el:
            return middle_idx
        elif target > middle_el:
            return self.search_bounded(nums, target, middle_idx + 1, top)
        else:
            return self.search_bounded(nums, target, bot, middle_idx)



    def search(self, nums: List[int], target: int) -> int:
        return self.search_bounded(nums, target, 0, len(nums))