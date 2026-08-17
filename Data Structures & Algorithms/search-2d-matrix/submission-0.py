'''
an m * n matrix thats sorted by rows first can really be treated as a m*n long array

to convert an index in (0, m*n) to 2d indexes in (0,m rows) (0, n cols) we use:
- (idx // n) = row
- (idx % n) = col

perform a normal binary search indexing into the matrix as a flat list
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        def flat_idx_to_matrix_indices(idx: int):
            # requires: matrix has atleast 1 row
            assert idx < m*n

            return (idx // n, idx % n)

        def binary_search(bot: int, top: int):
            if top < bot:
                return False

            mid = (top + bot) // 2
            mid_row, mid_col = flat_idx_to_matrix_indices(mid)
            mid_val = matrix[mid_row][mid_col]

            if mid_val == target:
                return True
            if mid_val < target:
                return binary_search(mid+1, top)
            else:
                return binary_search(bot, mid-1)

        m = len(matrix)
        n = len(matrix[0])

        return binary_search(0, m*n-1)


