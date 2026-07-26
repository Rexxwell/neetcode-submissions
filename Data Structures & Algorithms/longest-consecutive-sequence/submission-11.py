class Solution:
    # Using `num - 1`
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        
        for num in nums_set:
            if num - 1 in nums_set:
                # This is not a start to a sequence
                continue
            
            length = 1
            target_num = num + 1

            while target_num in nums_set:
                length += 1
                target_num += 1
            
            if length > max_length:
                max_length = length

        return max_length
            