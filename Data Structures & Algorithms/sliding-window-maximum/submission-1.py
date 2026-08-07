class Solution:
    # Brute Force
    # Runtime: TLE
    # Memory: TLE
    # Time Complexity: O(n * k)
    # Space Complexity: O(k) auxiliary space
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements = []
        i = 0
        j = k - 1

        while j < len(nums):
            window = []

            for l in range(i, j + 1):
                window.append(nums[l])
            
            max_elements.append(max(window))
            i += 1
            j += 1

        return max_elements