class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #initialize left and right
        left, right = 0, len(matrix) -1
        target_row = -1
        #run loop as long as left is less than or equal to right:
        while left <= right:
            #find the middle row, check left+right //2
            middle = (left + right) // 2
            
            #if the target is greater than the first value and less than the last value of this row
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                #return this row
                target_row = middle
                break
            #else if target is greater than the last element of this row:
            elif target > matrix[middle][-1]:
                #update left to middle + 1
                left = middle + 1
            #else if target is smaller than the first element of this row:
            else:
                #update right to middle - 1
                right = middle - 1
        if target_row == -1:
            return False

        
        #initialize row_left and row_right
        row_left, row_right = 0, len(matrix[target_row])-1
        #run loop as long as low left is less than or equal to right:
        while row_left <= row_right:
            #find the middle integer in our targer row
            row_middle = (row_left + row_right) // 2
            #if the middle integer is equal to our target:
            if matrix[target_row][row_middle] == target:
                #return True
                return True
            #elif middle integer is greater than our target:
            elif target > matrix[target_row][row_middle]:
                #update row_left = row_middle + 1
                row_left = row_middle + 1
            #else:
            else:
                #update row_right = row_middle - 1
                row_right = row_middle - 1
        #return False if we don't find our targer
        return False
