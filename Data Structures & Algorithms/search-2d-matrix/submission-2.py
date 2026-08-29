class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row = 0
        right_row = len(matrix) -1
        target_row = -1

        while left_row <= right_row:
            mid = (left_row + right_row) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = matrix[mid]
                break
            elif matrix[mid][0] > target:
                right_row = mid - 1
            elif matrix[mid][-1] < target:
                left_row = mid + 1
        if target_row == -1:
            return False
        
        left = 0
        right = len(target_row) - 1

        while left <= right:
            mid = (left + right) // 2

            if target_row[mid] == target:
                return True
            elif target_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False