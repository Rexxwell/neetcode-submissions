class Solution:
    # Hash Map
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for count in counts.values():
            if count > 1:
                return True
        return False