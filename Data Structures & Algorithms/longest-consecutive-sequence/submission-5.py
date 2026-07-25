class Solution:
    # Brute Force using `in` operator
    # Solution with no AI
    # Runtime: 386ms
    # Memory: 7.9 MB
    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0

        for num in nums:
            length = 1
            target_num = num + 1

            while target_num in nums:
                length += 1
                target_num += 1
            
            if length > max_length:
                max_length = length
        
        return max_length