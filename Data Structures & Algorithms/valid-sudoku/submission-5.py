class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if (len(board) == 0):
            return true

        rows = [set() for _ in range (9)]
        cols = [set() for _ in range (9)]
        boxes = [[set() for __ in range (3)] for _ in range (3)]
        print(len(board))
        print(len(board[0]))
        print(boxes)

        for y in range(len(board)):
            for x in range (len(board[0])):
                val = board[x][y]
                if val == '.':
                    continue
                    
                print(x, y, val)
                in_row = val in rows[y]
                in_col = val in cols[x]
                in_box = val in boxes[x // 3][y // 3]
                if (in_row or in_col or in_box):
                    return False
                
                rows[y].add(val)
                cols[x].add(val)
                boxes[x // 3][y // 3].add(val)

        return True
                    
                