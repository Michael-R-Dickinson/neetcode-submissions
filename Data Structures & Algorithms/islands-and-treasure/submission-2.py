from collections import deque

'''
breadth first search from each treasure chest
give each cell the value of min(the distance to the treasure chest, current value) such that each cell ends with the value to the nearest chest

do we use a visisted set? No - multiple treasure chests can reach a single land cell, each cell must reflect the closeness to the NEAREST chest

solution: O(m*n*num_treasures)

'''

INT_MAX = 2**31 - 1
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:   
        if len(grid) == 0:
            return grid

        m = len(grid)
        n = len(grid[0])

        treasures = []
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 0:
                    treasures.append((y,x))
  
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        queue = deque()
        queue.extend(treasures)

        visited = set()

        steps_taken = 0

        while queue:
            for i in range(len(queue)):
                y, x = queue.popleft()
                val = grid[y][x]

                if val == -1:
                    continue
                if (y,x) in visited:
                    continue
                
                visited.add((y,x))

                for y_offset, x_offset in directions:
                    neighbor_y, neighbor_x = y+y_offset, x+x_offset
                    if neighbor_y < 0 or neighbor_y >= m:
                        continue
                    if neighbor_x < 0 or neighbor_x >= n:
                        continue

                    queue.append((neighbor_y, neighbor_x))

                if val != 0:
                    grid[y][x] = min(steps_taken, val)

            steps_taken += 1
    

                
                

