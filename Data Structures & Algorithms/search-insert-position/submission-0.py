class Solution:
    def binarySearchRange(self, nums, target, bot, top):
        size = top - bot
        if size <= 0:
            # couldn't find el
            return bot

        mid = bot + (size // 2)
        middle_el = nums[mid]

        if target == middle_el:
            return mid
        elif target > middle_el:
            return self.binarySearchRange(nums, target, mid + 1, top)
        else:
            return self.binarySearchRange(nums, target, bot, mid)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearchRange(nums, target, 0, len(nums))