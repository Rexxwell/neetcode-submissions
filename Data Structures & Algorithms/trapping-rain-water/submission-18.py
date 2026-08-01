class Solution:
    # Brute Force
    # Runtime: 79ms
    # Memory: 8.2 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def trap(self, height: List[int]) -> int:
        water_area = 0

        for i in range(1, len(height) - 1):
            l_heights = []
            r_heights = []

            for j in range(i):
                l_heights.append(height[j])
            
            for k in range(i + 1, len(height)):
                r_heights.append(height[k])
            
            l_max = max(l_heights)
            r_max = max(r_heights)
            l_height = l_max if l_max > height[i] else -1
            r_height = r_max if r_max > height[i] else -1

            if l_height != -1 and r_height != -1:
                water_area += min(l_height, r_height) - height[i]

        return water_area