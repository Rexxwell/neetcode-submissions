class Solution:
    # Binary Search
    # Runtime: 31ms
    # Memory: 8.7 MB
    # Time Complexity: O(logm + logn) = O(log(m * n))
    # Space Complexity: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        matrix_i = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            x = matrix[mid][0]
            y = matrix[mid][-1]

            if x <= target and target <= y:
                matrix_i = mid
                break
            elif x > target:
                high = mid - 1
            elif x < target:
                low = mid + 1

        low = 0
        high = len(matrix[matrix_i]) - 1

        while low <= high:
            mid = low + (high - low) // 2
            num = matrix[matrix_i][mid]

            if num == target:
                return True
            elif num > target:
                high = mid - 1
            elif num < target:
                low = mid + 1
        
        return False