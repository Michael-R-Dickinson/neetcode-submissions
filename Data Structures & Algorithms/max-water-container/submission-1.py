class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # moving the pointer with a higher height will not increase the volume
        # thus we should always move the lower pointer as this gives us the opportunity
        # to find a better solution
        # especially since, moving any pointer inwards, decreases the width of the section
        # which lowers one factor in the volume

        # use two pointers, from each end and track the maximum volume achieved while
        # always moving the lower pointer inwards

        max_volume = 0
        l = 0
        r = len(heights) - 1
        runs = 0
        while l < r:
            r_height = heights[r]
            l_height = heights[l]

            volume = (r - l) * min(r_height, l_height)
            max_volume = max(max_volume, volume)

            print(l, r, 'heights: ', l_height, r_height)
            if l_height > r_height:
                r -= 1
            elif l_height < r_height:
                l += 1
            else:
                r-= 1
                l += 1

        return max_volume
