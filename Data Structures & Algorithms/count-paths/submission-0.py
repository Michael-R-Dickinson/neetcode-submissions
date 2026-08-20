'''
number of UNIQUE paths

down or right only - so you can never backtrack

target is always bottom right

grid is m x n

recurrence relation: at each step we should simplify the problem - it should never get more complex - this fits the structure of this problem
- each move gets closer to the target!

number_of_unique_paths_from_position_to_target(x,y):
R(x+1, y)
+
R(x, y+1) - note y increases downwards

base cases:
- made to target: x=n, y=m - note x and y are 1 indexed so they start at 1,1 - num paths += 1
- outside of the board: num paths = 0
    - y>m
    - x>n

Notation:
- y increases downwards
- x and y are 1 indexed

'''


from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(maxsize=None)
        def number_of_unique_paths_from_position_to_target(x: int, y: int)->int:
            if x == n and y == m:
                return 1 # we found a path

            if x > n or y > m:
                return 0 # no paths if we're outside the board
            
            down_paths = number_of_unique_paths_from_position_to_target(
                x,
                y + 1
            )

            right_paths = number_of_unique_paths_from_position_to_target(
                x + 1,
                y
            )
            return down_paths + right_paths
        
        return number_of_unique_paths_from_position_to_target(1,1)



