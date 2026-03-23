class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row_idx in range(0, len(grid)):
            row = grid[row_idx]
            for col_idx in range(0, len(row)):
                if row[col_idx] == 1:
                    perimeter = perimeter + 1 if Solution.check_right(row, col_idx) else perimeter
                    perimeter = perimeter + 1 if Solution.check_left(row, col_idx) else perimeter
                    perimeter = perimeter + 1 if Solution.check_up(grid, row_idx, col_idx) else perimeter
                    perimeter = perimeter + 1 if Solution.check_down(grid, row_idx, col_idx) else perimeter
        return perimeter
    
    @staticmethod
    def check_down(grid, row_idx, col_idx):
        return row_idx + 1 >= len(grid) or grid[row_idx+1][col_idx] == 0
    @staticmethod
    def check_up(grid, row_idx, col_idx):
        return row_idx - 1 < 0 or grid[row_idx -1][col_idx] == 0
    @staticmethod
    def check_left(row, col_idx):
        return col_idx-1 < 0 or row[col_idx-1] == 0
    @staticmethod
    def check_right(row, col_idx):
        return col_idx+1 >= len(row) or row[col_idx+1] == 0
