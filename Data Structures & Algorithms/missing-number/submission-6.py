class Solution:
    # Mathematical Way (Sum Formula)
    # Find the sum of the nums array. Find the expected sum of the 
    # nums array if we assumed that all the numbers are present.
    # This works because we know that if there are n numbers in the list,
    # we already know the expected range of numbers `nums` is supposed to have.
    # Thus, we can use this information to compare which number is missing by
    # finding the difference in the actual and expected sum.
    # Runtime: 50ms
    # Memory: 7.6 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) / 2
        actual_sum = 0
        for num in nums:
            actual_sum += num
        
        return int(expected_sum - actual_sum)