class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left < right:
            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] >= target:
                right = mid
            else:
                left = mid + 1
                
        
        row = matrix[left]

        left = 0
        right = len(row) - 1
        print(row)

        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False