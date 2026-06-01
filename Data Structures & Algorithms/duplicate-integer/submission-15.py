class Solution:
    # In python, when you convert a list into a set,
    # it removes all the duplicate elements.
    # If there are duplicates, then the length of the set(nums)
    # will be lesser then the length of the list nums.
    #
    # Time complexity: O(n)
    # Space complexity: O(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)