'''
Min possible value:
- max(weights)
Max possible value: 
- sum(weights)

Linear sweep:
m = sum(weights)
n = len(weights)
O(m * n)

Binary Search:
O(log(m) * n)

binary search to find the value of capacity such that:
- capacity can ship all packages within days
- any value lower than it would fail

binary search variant:
- get the midpoint - simulate shipping packages to determine if we can ship all packages with the given capacity
if (we can ship): search lower values of capacity
if (we can't ship): search higher values of capacity

termination condition:
- [1 2 3 4 5 6]

'''


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_to_ship_with_capacity(capacity):
            days = 1
            i = 0
            current_load = 0
            while i < len(weights):
                weight = weights[i]
                if current_load + weight > capacity:
                    # push this weight off to a new day
                    current_load = weight
                    days += 1
                else:
                    current_load += weight
                i += 1
            return days
                

        def binary_search(bot, top):
            if bot > top:
                return bot
            
            mid = bot + (top - bot) // 2
            days_to_ship = days_to_ship_with_capacity(mid)

            if days_to_ship <= days:
                return binary_search(bot, mid-1)
            else:
                return binary_search(mid+1, top)
        
        return binary_search(max(weights), sum(weights))
        