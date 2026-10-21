'''
traverse up from the oceans to see which cells are can reach that ocean
- a cell that can't reach an ocean is LOWER than neighboring cells that can

keep track of which cells have been visited - reset between traversing from each ocean

'''

from functools import cache

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs_from_ocean(y,x, ocean_name):
            # base case
            # if y < 0 or y >= m:
            #     return
            # if x < 0 or x >= n:
            #     return 

            if (y,x) in visited:
                return
            
            # add to visited
            visited.add((y,x))

            # mark node as reachable by ocean with ocean_idx
            reachable[ocean_name].add((y,x))
            # traverse onto nearby neighbors which are >= current node's height
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for offset_y, offset_x in directions:
                neighbor_y = y + offset_y
                neighbor_x = x + offset_x
                if neighbor_y < 0 or neighbor_y >= m or neighbor_x < 0 or neighbor_x >= n:
                    continue

                if heights[neighbor_y][neighbor_x] >= heights[y][x]:
                    dfs_from_ocean(neighbor_y, neighbor_x, ocean)

        reachable = {
            'atlantic': set(),
            'pacific': set()
        }
        if len(heights) == 0:
            return []
        m = len(heights)
        n = len(heights[0])

        edges = {
            'pacific': [(0, i) for i in range(n)] + [(i,0) for i in range(m)], 
            'atlantic': [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m)]
        }

        for ocean in reachable.keys():
            visited = set()
            for y,x in edges[ocean]:
                dfs_from_ocean(y,x, ocean)
        
        reachable_from_both = reachable['atlantic'].intersection(reachable['pacific'])
        return list(reachable_from_both)


