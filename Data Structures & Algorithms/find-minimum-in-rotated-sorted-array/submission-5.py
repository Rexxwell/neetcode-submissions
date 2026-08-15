class Solution:
    # Binary Search
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    # n is the length of nums
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                # low and mid are in the same segment
                # high is in a different segment
                # the minimum element must be in the [mid + 1, high] range
                low = mid + 1
            else:
                # mid and high are in the same segment
                # low is in a different segment
                # the minimum element must be in the [low, mid] range
                high = mid

        return nums[low]