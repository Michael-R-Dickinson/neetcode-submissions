"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


'''

qs:
- qauranteed square - yes
- even number of rows/cols - yes

solve recursively
- each subproblem is a smaller square
- create each smaller square by giving it a range of indices: get square size via floor division
    x,y format - index into matrix
    (x_min, x_max), (y_min, y_max)
        - top_left: (x_min, x_min + len_x // 2 + 1), (y_min, y_min + len_y // 2 + 1)
        - bottom_right: (x_min + len_x // 2 + 1, x_max), (y_min + ...)
- once we reach a single square - return its value - not a node
- only construct a node when we receive returns from children that are not all the same value
    - determine if the current square is a leaf: are all of its values the same
- 
'''

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def constructQuadTree(x_min, x_max, y_min, y_max) -> 'Node':
            '''
            returns: Node if we constructed a node from this grid
                - when not all values were the same (or if any were nodes)
                - else value: 0 or 1
            '''
            
            x_range = x_max - x_min + 1
            x_mid = x_min + (x_range // 2)

            y_range = y_max - y_min + 1
            y_mid = y_min + (y_range // 2)

            # check if all are equal within the grid
            above_block = sumMatrix[y_min-1][x_max] if y_min-1 >= 0 else 0
            left_block = sumMatrix[y_max][x_min-1] if x_min-1 >= 0 else 0
            above_left_corner = sumMatrix[y_min-1][x_min-1] if y_min-1 >= 0 and x_min-1 >= 0 else 0
            sumOfSquares = sumMatrix[y_max][x_max] - above_block - left_block + above_left_corner
            if sumOfSquares == 0 or sumOfSquares == x_range * y_range:
                return Node(grid[y_min][x_min], True, None, None, None, None)

            top_left = constructQuadTree(x_min, x_mid - 1, y_min, y_mid - 1)
            top_right = constructQuadTree(x_mid, x_max, y_min, y_mid - 1)
            bottom_left = constructQuadTree(x_min, x_mid - 1, y_mid, y_max)
            bottom_right = constructQuadTree(x_mid, x_max, y_mid, y_max)

            # quadrants aren't equal, assemble a new node with them
            return Node(1, False, top_left, top_right, bottom_left, bottom_right)

        n = len(grid)
        if n == 0:
            return None

        # sumMatrix with the invariant: M[i,j] = sum of rows (0,i) within cols (0,i)
        sumMatrix = [([0] * n) for _ in range(n)]
        # init with 1st row and col filled in - avoids indexing errors
        sumMatrix[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            sumMatrix[i][0] = grid[i][0] + sumMatrix[i-1][0]
            sumMatrix[0][i] = grid[0][i] + sumMatrix[0][i-1]
        for row in range(1, len(grid)):
            for col in range(1, len(grid)):
                sumMatrix[row][col] = grid[row][col] + sumMatrix[row][col-1] + sumMatrix[row-1][col] - sumMatrix[row-1][col-1]
        tree = constructQuadTree(0, len(grid[0]) -1, 0, len(grid) -1)
        return tree
            


        