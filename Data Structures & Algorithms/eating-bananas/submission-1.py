'''
computation for a single k:
ceiling divide each pile by k. The sum of this array = the number of hours required to finish all piles
-> given this computation is fast: O(n) for the sum, we could binary search it. 
-> O(nlog n)
'''

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def computeHoursRequired(k):
            return sum(math.ceil(pile / k) for pile in piles)

        def binarySearchKValues(bot, top):
            '''
            we binary search for the minimum k value that allows us to eat all bananas in h hours. 
            We do this by searching for smaller k's if we've found a valid k, and larger ks if we found an invalid k. Whenever we find a valid, k, we log it in minValidK such that when the function returns, minValidK is the minimum valid k allowing us to eat piles in h hours.
            '''

            nonlocal minValidK

            if top < bot:
                return
            
            mid = (top + bot) // 2
            hours_required_for_k = computeHoursRequired(mid)
            if hours_required_for_k <= h:
                # ate too fast -> search for lower k
                minValidK = mid
                binarySearchKValues(bot, mid-1)
            else:
                # ate too slow
                binarySearchKValues(mid+1, top)
            
        minValidK = float('inf')
        max_possible_k = 10_000 * 1_000_000_000
        binarySearchKValues(1, max_possible_k)

        return minValidK
