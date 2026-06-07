class Solution:
    # Meta Binary Search
    # - Finds any occurence index of the target if there are duplicates of the target in nums
    # Runtime: 38 ms
    # Memory: 7.7 MB
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        # If nums = None, then it would evaluate as False in boolean.
        if (not nums):
            return -1

        # Find the highest jumpSize (power of 2) we can do for the nums array
        # without getting an index out of bounds error.
        jumpSize = 1
        while (jumpSize < len(nums)):
            jumpSize *= 2

        # We start at i = -1 so that nums[0] will be checked.
        i = -1

        # We check if jumpSize > 0 because in the last iteration when jumpSize = 1,
        # 1 // 2 = 0 and 0 is not a valid jump we can make.
        while (jumpSize > 0):
            # We make a new variable iJump to see if the jump we will make is valid or not.
            # Remember, i is the index where it is guaranteed that nums[i] <= target if i != -1.
            # If i == -1, then the target does not exist in the nums array.
            iJump = i + jumpSize

            # We also check if iJump < len(nums) because we need to make sure the jump we make
            # is within the index of the nums array.
            # There is a case where we take the first jump (biggest jump) and then
            # the second jump will most likely be out of index if we take it.
            if (iJump < len(nums) and nums[iJump] < target):
                i = iJump

            # If nums[iJump] == target, then we just return iJump immediately.
            # Though, if there are duplicates of target in the nums array, then
            # we would just be immediately returning the index of any occurence of target
            # in nums array.
            elif (iJump < len(nums) and nums[iJump] == target):
                return iJump

            # We take jumps from the highest power of 2 to the lowest power of 2.
            jumpSize //= 2

        # If i == -1, then that means that we did not take any jumps at all
        # because the num in nums array are all > target. So, we don't take any jumps at all
        # and the target does not exist in the nums array.
        # Remember, since nums[i] after the while loop only guarantees that nums[i] <= target if
        # i != -1, we also have to check if nums[i] == target to make sure we found the target.
        if (i != -1 and nums[i] == target):
            return i
        return -1