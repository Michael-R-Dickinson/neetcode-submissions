'''
begin searching for unordered spot

INVARIANT for our search for the pivot: right < left:
    the pivot is in the middle
    check the middle element
        - mid < left - split IS between left...mid
        - mid > right - split IS between mid...right
        - base case: two adjacent elements with right<left - we found the pivot
    
else:
    the pivot is not between right...left

[1 2 3 4 5 6] -> special case? where our invariant that right < left isn't satisfied
- pivot is at the last idx

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchForPivot(left: int, right: int):
            # inclusive left and right
            if right - left + 1 == 2:
                assert nums[left] > nums[right]
                return right
            
            mid = (left + right) // 2
            midval = nums[mid]
            if midval < nums[left]:
                # search between left... mid
                return searchForPivot(left, mid)
            if midval > nums[right]:
                return searchForPivot(mid, right)
            assert False, "we made a mistake"
        
        def index_into_rotated(idx):
            return (idx + pivot_idx) % len(nums)
            
        def binarySearch(left: int, right: int):
            if right < left:
                return -1
            
            mid = (right + left) // 2
            midval = nums[index_into_rotated(mid)]
            leftval = nums[index_into_rotated(left)]
            rightval = nums[index_into_rotated(right)]

            if midval == target:
                return mid
            if midval > target:
                return binarySearch(left, mid-1)
            else:
                return binarySearch(mid+1, right)
                
        
        if not nums:
            return -1
        # if len(nums)==1:
        #     return 0 if nums[0] == target else -1
        
        pivot_idx = 0
        if nums[0] <= nums[-1]:
            # pivot is the end of the list
            pivot_idx = 0
        else:
            pivot_idx = searchForPivot(0, len(nums)-1)
            
        result = binarySearch(0, len(nums)-1)
        if result == -1:
            return result
        return index_into_rotated(result)
