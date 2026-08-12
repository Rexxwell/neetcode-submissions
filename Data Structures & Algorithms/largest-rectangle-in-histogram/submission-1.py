class Solution:
    # Brute Force
    # Runtime: 2558ms, TLE
    # Memory: 9.7 MB, TLE
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_rectangle_area = 0

        for i in range(len(heights)):
            height_i = heights[i]
            left_boundary = i

            for j in range(i - 1, -1, -1):
                height_j = heights[j]

                if height_j >= height_i:
                    left_boundary -= 1
                else:
                    break
            
            right_boundary = i
            
            for k in range(i + 1, len(heights)):
                height_k = heights[k]

                if height_k >= height_i:
                    right_boundary += 1
                else:
                    break
            
            rectangle_area = (right_boundary - left_boundary + 1) * height_i
            largest_rectangle_area = max(rectangle_area, largest_rectangle_area)

        return largest_rectangle_area