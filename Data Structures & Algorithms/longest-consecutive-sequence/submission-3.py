class Solution:
    # Brute Force
    # Solution with no AI
    # Runtime: 1252ms
    # Memory: 8.0 MB
    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0

        for num in nums:
            i = 0
            length = 1
            target_num = num + 1

            while i < len(nums):
                if nums[i] == target_num:
                    length += 1
                    target_num += 1
                    i = 0
                else:
                    i += 1
            
            if length > max_length:
                max_length = length
    
        return max_length
                