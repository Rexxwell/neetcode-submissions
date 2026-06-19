import heapq

class Solution:
    # Max Heap
    # Runtime: 28ms
    # Memory: 7.9 MB
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = [-stone for stone in stones] # O(n)
        heapq.heapify(stonesHeap) # O(n)
        while (len(stonesHeap) >= 2): # O(n)
            x = heapq.heappop(stonesHeap) * -1 # O(logn)
            y = heapq.heappop(stonesHeap) * -1
            diff = abs(x - y)
            if (diff > 0):
                heapq.heappush(stonesHeap, diff * -1) # O(logn)
        return 0 if len(stonesHeap) == 0 else stonesHeap[0] * -1