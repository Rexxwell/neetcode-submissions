class Solution:
    # Meta Binary Search
    # - Finds the first occurence index of the target if there are duplicates of the target in nums
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
            # Remember, i is the index where it is guaranteed that nums[i] < target if i != -1.
            # If i == -1, then the target does not exist in the nums array.
            iJump = i + jumpSize

            # We also check if iJump < len(nums) because we need to make sure the jump we make
            # is within the index of the nums array.
            # There is a case where we take the first jump (biggest jump) and then
            # the second jump will most likely be out of index if we take it.
            if (iJump < len(nums) and nums[iJump] < target):
                i = iJump

            # We take jumps from the highest power of 2 to the lowest power of 2.
            jumpSize //= 2

        # Since it is guaranteed that nums[i] < target from the if statement above.
        # That means our target, if it exists, should lie on i += 1, the index to the right.
        i += 1

        # Since nums[i] is guaranteed to have our target value if it exists.
        # We only need to check if nums[i] == target and if i < len(nums)
        # so that we don't hit that edge case where it goes index out of bounds.
        if (i < len(nums) and nums[i] == target):
            return i
        return -1