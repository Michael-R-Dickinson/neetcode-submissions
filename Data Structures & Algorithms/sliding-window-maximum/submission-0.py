# we need to keep track of the biggest element in the window
# max heaps do that
# so when an element enters the window - add to heap
# when it exits, remove from heap
# read off top 1 element

# time complexity: we add/remove each element once at most - adding to a heap is O(log(n))
# total: O(n*log(n))

from heapq import heappush, heappop, heapify

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # init window
        window = [-n for n in nums[0 : k]]
        heapify(window)

        out = [-1] * (len(nums) - k + 1)

        l = 0
        out[l] = -window[0]
        for r in range(k, len(nums)):
            # add r to window
            heappush(window, -nums[r])
            # remove l from window
            window.remove(-nums[l])
            heapify(window)
            l += 1

            # check state
            out[l] = -window[0]
        return out


            
