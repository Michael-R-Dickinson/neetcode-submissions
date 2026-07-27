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
        def constructQuadTree(x_min, x_max, y_min, y_max) -> 'Node' | int:
            '''
            returns: Node if we constructed a node from this grid
                - when not all values were the same (or if any were nodes)
                - else value: 0 or 1
            '''

            # single square
            print(x_min, x_max, y_min, y_max)
            if x_min == x_max:
                return grid[y_min][x_min]
            
            x_range = x_max - x_min + 1
            x_mid = x_min + (x_range // 2)
            
            y_range = y_max - y_min + 1
            y_mid = y_min + (y_range // 2)

            top_left = constructQuadTree(x_min, x_mid - 1, y_min, y_mid - 1)
            top_right = constructQuadTree(x_mid, x_max, y_min, y_mid - 1)
            bottom_left = constructQuadTree(x_min, x_mid - 1, y_mid, y_max)
            bottom_right = constructQuadTree(x_mid, x_max, y_mid, y_max)

            quadrants = [top_left, top_right, bottom_left, bottom_right]
            quadrants_are_equal = True
            prev_quadrant = None
            for quadrant in quadrants:
                if not isinstance(quadrant, int):
                    quadrants_are_equal = False
                    break
                if quadrant == prev_quadrant or prev_quadrant is None:
                    prev_quadrant = quadrant
                else:
                    quadrants_are_equal = False
                    break
            
            if quadrants_are_equal:
                return top_right # return the shared value of all quadrants
            # quadrants aren't equal - they might be nodes or just ints
            # but we need to construct a node from them
            for i, quadrant in enumerate(quadrants):
                if isinstance(quadrant, int):
                    quadrants[i] = Node(
                        quadrant, True, 
                        None, None, None, None
                    )
            return Node(1, False, quadrants[0], quadrants[1], quadrants[2], quadrants[3])
        
        if len(grid) == 0:
            return None
        tree = constructQuadTree(0, len(grid[0]) -1, 0, len(grid) -1)
        if isinstance(tree, int):
            return Node(tree, True, None, None, None, None)
        return tree
            


        