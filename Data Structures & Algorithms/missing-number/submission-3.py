class Solution:
    # Manually Checking Iteration
    # Runtime: 42ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing_num = 0
        for i in range(n + 1):
            if missing_num not in nums:
                return missing_num
            missing_num += 1