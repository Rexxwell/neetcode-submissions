class Solution:
    # Sorting
    # Time complexity:
    #   Worst Case - O(nlogn)
    #   Average Case - O(nlogn)
    #   Base Case - O(n)
    # Space complexity: O(1)
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True
        return False