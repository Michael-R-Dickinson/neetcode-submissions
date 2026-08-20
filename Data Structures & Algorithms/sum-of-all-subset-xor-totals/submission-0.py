'''
how do we get all possible subsets of an array?

Solve recursively:
start with all n elements:
make n recursive calls:
- each one removes the ith element
uniqueness is gauranteed because each recursive call is MISSING an element that all others has. 


'''



class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_total_sum = 0
        n = len(nums)
        # shift the 1 over n times such that there are n digits
        for subset_mask in range(1<< n):
            xor_total = 0
            for idx, num in enumerate(nums):
                if ((1 << idx) & subset_mask) != 0:
                    xor_total = xor_total ^ num
            xor_total_sum += xor_total
        return xor_total_sum
        
