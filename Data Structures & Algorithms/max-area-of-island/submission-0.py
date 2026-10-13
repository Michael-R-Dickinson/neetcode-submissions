class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area_of_island(y, x):
            if y<0 or y>=m:
                return 0
            if x<0 or x>=n:
                return 0
            if grid[y][x] == 0:
                return 0
            if (y,x) in visited:
                return 0
            
            visited.add((y,x))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            area = 1
            for y_offset, x_offset in directions:
                area += area_of_island(y+y_offset, x+x_offset)
            
            return area
        
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])

        visited = set()
        max_area = 0
        for y in range(m):
            for x in range(n):
                max_area = max(max_area, area_of_island(y,x))
                
        return max_area