class Solution:
    # Brute Force
    # Runtime: 47ms
    # Memory: 8.9 MB
    # Time Complexity: O(nm)
    # Space Complexity: O(1)
    # n is the length of matrix
    # m is the length of each list in matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for num in row:
                if num == target:
                    return True
        
        return False