class Solution:
    # Binary Search (Finding the cut properly)
    # Runtime: 29ms
    # Memory: 7.9 MB
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    # n is the length of nums
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            num_mid = nums[mid]
            num_high = nums[high]

            if num_mid > num_high:
                # low and mid are in the same segment
                # high is in a different segment
                # minimum element must be in the right segment
                low = mid + 1
            elif num_mid <= num_high:
                # low is in a different segment
                # mid and high are in the same segment
                # minimum element must in the left segment or mid itself
                high = mid

        if low == 0:
            # nums has one segement
            low = 0
            high = len(nums) - 1
        else:
            # nums has two segments
            
            if nums[0] <= target <= nums[low - 1]:
                high = low - 1
                low = 0
            elif nums[low] <= target <= nums[len(nums) - 1]:
                low = low
                high = len(nums) - 1
            else:
                return -1

        while low <= high:
            mid = low + (high - low) // 2
            num_mid = nums[mid]

            if num_mid == target:
                return mid
            elif num_mid < target:
                low = mid + 1
            elif num_mid > target:
                high = mid - 1

        return -1