'''
count perimiter edges:
- for each island tile. Count how many "exposed" edges it has - edges without a neighbor that is land
sum(exposed_edges)=perimiter

(because there aren't lakes)

step1: find an island tile
step2: dfs over island tiles, and for each tile, count its exposed edges

maintain a list of visited tiles so we don't loop
'''


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def isOutOfBounds(y,x)->bool:
            return y >= len(grid) or x >= len(grid[0]) or y < 0 or x < 0

        def searchForIsland(y,x)->tuple[int, int]:
            if isOutOfBounds(y,x) or (y,x) in visited:
                return None
            if grid[y][x] == 1:
                return (y,x)
            
            visited.add((y,x))
            
            for y_offset, x_offset in [(0,1),(0,-1), (1,0), (-1, 0)]:
                search_direction = searchForIsland(y + y_offset, x + x_offset)
                if search_direction is not None:
                    return search_direction
            return None   

        def calculatePerimiter(y,x)->int:
            if isOutOfBounds(y,x) or grid[y][x] == 0 or (y,x) in visited:
                return 0
            
            visited.add((y,x))
            
            perimiter = 0
            for y_offset, x_offset in [(0,1),(0,-1), (1,0), (-1, 0)]:
                check_y = y + y_offset
                check_x = x + x_offset
                if isOutOfBounds(check_y, check_x) or grid[check_y][check_x] == 0:
                    perimiter += 1
                else:
                    perimiter += calculatePerimiter(check_y, check_x)
            return perimiter

        if not grid:
            return 0
        visited = set()
        island_y, island_x = searchForIsland(len(grid) // 2, len(grid[0]) //2)

        visited = set()
        return calculatePerimiter(island_y, island_x)
