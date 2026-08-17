'''
target = 5
[-1,0,2,4,6,8]

we always check the value at index insert+1 last
'''



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # inclusive indexing
        def binSearch(bot, top):
            if top < bot:
                # number cannot be found
                return bot

            mid = (top + bot) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            if mid_val < target:
                return binSearch(mid+1, top)
            else:
                return binSearch(bot, mid-1)

        return binSearch(0, len(nums)-1)