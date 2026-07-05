class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        min_so_far = float('inf')
        for sell in range(len(prices)):
            min_so_far = min(min_so_far, prices[sell])
            best = max(best, prices[sell] - min_so_far)
        return best

