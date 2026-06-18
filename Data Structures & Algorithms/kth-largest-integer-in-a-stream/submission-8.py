import bisect

# The Sorted Array (Binary Search + Insertion Sort)
# Runtime: 33ms
# Memory: 8.0 MB
class KthLargest:

    # Time Complexity:
    #   Best Case: O(n)
    #   Average Case: O(logn)
    #   Worst Case: O(nlogn) 
    # Space Complexity:
    #   Initially: O(n)
    #   After: O(k)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
        self.nums = self.nums[-self.k:]

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        if (len(self.nums) > self.k):
            self.nums.pop(0)
        return self.nums[0]