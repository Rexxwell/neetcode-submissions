class Solution:
    # Brute Force
    # Runtime: 27ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1