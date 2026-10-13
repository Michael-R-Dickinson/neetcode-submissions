'''
iterate through every edge cell
- begin a dfs outwards:
    - mark it visited
    - dfs only to adjacent neighbors that are "O"s

iterate through the whole grid
for each O we find:
    if it is not in visited, make it an X - because it is surrounded
'''



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs_from_edge(y,x) -> None:
            if y<0 or y>=m or x<0 or x>=n:
                return
            if board[y][x] != "O":
                return
            if (y,x) in visited:
                return
            
            visited.add((y,x))

            directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
            for offset_y, offset_x in directions:
                dfs_from_edge(y+offset_y, x+offset_x)
        
        directions = [(0,1), (1, 0), (0,-1), (-1, 0)]
        m = len(board)
        n = len(board[0])
        
        visited = set()
        direction_idx = 0
        borders_y = {(y,x) for y in range(m) for x in (0, n-1)} 
        borders_x = {(y,x) for x in range(n) for y in (0, m-1)}
        borders = borders_y | borders_x
        for y,x in borders:
            dfs_from_edge(y,x)
            
        for y in range(m):
            for x in range(n):
                if board[y][x] == "O" and (y,x) not in visited:
                    board[y][x] = "X"

        