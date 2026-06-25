"""
what if for each column, compute prefix sum for a fixed row

then for each row, compute prefix sum for fixed column
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_ = [list(matrix[row]) for row in range(len(matrix))]
        sum_ = self.sum_
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                left_sum = sum_[row][col - 1] if col - 1 >= 0 else 0
                sum_[row][col] = left_sum + matrix[row][col]

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                up_sum = sum_[row - 1][col] if row - 1 >= 0 else 0
                sum_[row][col] += up_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        above = self.sum_[row1 - 1][col2] if row1 - 1 >= 0 else 0
        left = (self.sum_[row2][col1 - 1] if col1 - 1 >= 0 else 0) - (
            self.sum_[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        )
        return self.sum_[row2][col2] - above - left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)