class Solution:
    # Brute force using `set()` for O(1) lookup on average
    # Solution with no AI
    # Runtime: 56ms
    # Memory: 8.0 MB
    # Time Complexity: O(n^2)
    # Space Complity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_checked = set()
        max_length = 0
        
        for num in nums:
            if num in nums_checked:
                continue
            
            nums_checked.add(num)
            length = 1
            target_num = num + 1

            while target_num in nums_set:
                target_num += 1
                length += 1

            if length > max_length:
                max_length = length

        return max_length