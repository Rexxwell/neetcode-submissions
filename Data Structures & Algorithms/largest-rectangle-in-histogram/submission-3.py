class Solution:
    # Monotonic stack
    # Runtime: 126ms
    # Memory: 10.3 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_rectangle_area = 0
        left_boundaries = [-1] * len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                left_boundaries[i] = stack[-1]

            stack.append(i)

        right_boundaries = [len(heights)] * len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                right_boundaries[i] = stack[-1]
            
            stack.append(i)
        
        for i in range(len(heights)):
            rectangle_area = ((right_boundaries[i] - 1) - (left_boundaries[i] + 1) + 1) * heights[i]
            largest_rectangle_area = max(rectangle_area, largest_rectangle_area)
            
        return largest_rectangle_area