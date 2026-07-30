class Solution:
    # Brute Force
    # Runtime: 123ms
    # Memory: 7.9 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for i in range(len(heights)):
            width = 1
            for j in range(i + 1, len(heights)):
                water = min(heights[i], heights[j]) * width
                
                if water > max_water:
                    max_water = water

                width += 1
        
        return max_water