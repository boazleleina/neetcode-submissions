class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first find the target row
        low, high = 0, len(matrix)-1
        target_row = -1
        while low<=high:
            mid = (low+high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break
            elif matrix[mid][-1] < target:
                low = mid+1
            else:
                high = mid-1
        if target_row == -1:
            return False
        
        row = matrix[target_row]
        row_l, row_h = 0, len(row)-1

        while row_l<= row_h:
            row_mid = (row_l+row_h)//2
            if row[row_mid] == target:
                return True
            elif row[row_mid] < target:
                row_l = row_mid + 1
            else:
                row_h = row_mid - 1
        return False