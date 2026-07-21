class Solution:
    # Optimized Prefix and Suffix
    # Runtime: 43ms
    # Memory: 7.9 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n), O(1) extra space excluding output
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        
        suffix = 1
        
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            output[i] *= suffix

        return output