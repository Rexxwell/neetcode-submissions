class Solution:
    # Hash Set
    # Time complexity: O(n)
    # Space complexity: O(n)
    #   if there are no duplicates, then you would add all the elements into the set.
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if (num in seen):
                return True
            seen.add(num)
        return False
