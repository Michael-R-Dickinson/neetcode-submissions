"""
loop over "steps"
at each step:
- get all rotten oranges
- mark all adjacent oranges for rotting

count the number of fresh fruits at the start
- subtract from this number every time we rot one

if we iterate over the whole grid for each step to find all rotten:
    - O(steps * m*n)

if we keep a growing list of rotten oranges rather than recomputing each step:
    - O(steps * m*n)
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot_adjacent(y, x):
            """
            go through each neighbor
            add it to to_rot if:
              - its within the grid
              - unrotted
            """
            directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
            for offset_y, offset_x in directions:
                if y+offset_y < 0 or y+offset_y >= m:
                    continue
                if x+offset_x < 0 or x+offset_x >= n:
                    continue
                if grid[y+offset_y][x+offset_x] != 1:
                    continue
                to_rot.add((y+offset_y, x+offset_x))

        m = len(grid)
        n = len(grid[0])
        fresh_fruits = sum(1 if grid[y][x] == 1 else 0 for y in range(m) for x in range(n))
        steps = 0
        while fresh_fruits > 0:
            to_rot = set()
            for y in range(m):
                for x in range(n):
                    if grid[y][x] == 2:
                        rot_adjacent(y, x)

            if len(to_rot) == 0:
                return -1
            for rot_y, rot_x in to_rot:
                grid[rot_y][rot_x] = 2
                fresh_fruits -= 1

            steps += 1
        return steps




