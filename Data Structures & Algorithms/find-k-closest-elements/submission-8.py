# Find the closest element to x: binary search
# Expand a window around the closest element to x based on:
# - add either the closest element on the left or right - whichever is smaller
# - stop when k elements are in the window - already sorted ascending

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) < k:
            return []

        # Binary Search
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == x:
                left = mid
                break
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        if left == 0:
            window_l = 0
        elif left == len(arr):
            window_l = left - 1
        else:
            window_l = left if abs(arr[left] - x) < abs(arr[left - 1] - x) else left - 1
        window_r = window_l
        print(left, left - 1)

        while window_r - window_l + 1 < k:
            if window_r == len(arr) - 1:
                window_l -= 1
                continue
            elif window_l == 0:
                window_r += 1
                continue

            right_dist_to_x = abs(arr[window_r + 1] - x)
            left_dist_to_x = abs(arr[window_l - 1] - x)
            if left_dist_to_x <= right_dist_to_x:
                window_l -= 1
            else:
                window_r += 1

        return arr[window_l : window_r + 1]
        
            




            
            