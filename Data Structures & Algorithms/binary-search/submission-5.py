class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # inclusive-inclusive indexing
        def binSearch(bot, top):
            if bot > top:
                return -1

            mid = (bot + top) // 2
            midval = nums[mid]
            
            if midval == target:
                return mid
            if midval < target:
                return binSearch(mid+1, top)
            else:
                return binSearch(bot, mid-1)

        return binSearch(0, len(nums)-1)
