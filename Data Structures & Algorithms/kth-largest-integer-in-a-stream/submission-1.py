import heapq

# Min-Heap
# Runtime: 27ms
# Memory: 7.7 MB
class KthLargest:

    # Time Complexity: O(n + (n-k)logn)
    # Space Complexity:
    #   Initially: O(n)
    #   After: O(k)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) # O(n)
        while (len(self.nums) > self.k): # O(n-k)
            heapq.heappop(self.nums) # O(logn)

    # Time Complexity: O(logk)
    # Space Complexity: O(k)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val) # O(logk)
        if (len(self.nums) > self.k):
            heapq.heappop(self.nums) #O(log(k+1))
        return self.nums[0]

        