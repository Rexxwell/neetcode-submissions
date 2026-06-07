class Solution:
    # Recursive Solution
    # Runtime: 38ms
    # Memory: 8.0 MB
    # Time Complexity: O(logn)
    # Space Complexity: O(logn)
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)
    
    def binarySearch(self, nums: List[int], target: int, startIndex: int, endIndex: int) -> int:
        if (startIndex <= endIndex):
            mid = (startIndex + endIndex) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                return self.binarySearch(nums, target, startIndex, mid - 1)
            else:
                return self.binarySearch(nums, target, mid + 1, endIndex)
        return -1