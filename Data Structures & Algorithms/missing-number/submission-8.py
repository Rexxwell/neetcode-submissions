class Solution:
    # Bit Manipulation (XOR)
    # Any number XORed with itself results in 0.
    # Any number XORed with 0 remains unchanged.
    # This works because we XOR the expected set against the actual set.
    # The expected set is the missing_number + i where missing_number = n
    # and i is [0, n - 1]. So the expected set is covered.
    # The actual set would be when we are XORing nums[i].
    # Runtime: 28ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = len(nums)
        for i in range(missing_number):
            missing_number = missing_number ^ i ^ nums[i]

        return missing_number