import heapq

class Solution:
    # Min Heap
    # Runtime: 30ms
    # Memory: 7.9 MB
    # Time Complexity: O(nlogk)
    #   It takes O(logk) worse case for heapq.heappush and heapq.heappop
    # Space Complexity: O(n + k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency = {}
        
        for num in nums:
            if num in nums_frequency:
                nums_frequency[num] += 1
            else:
                nums_frequency[num] = 1
        
        min_heap = []

        for num, frequency in nums_frequency.items():
            if len(min_heap) == k:
                heapq.heappush(min_heap, (frequency, num))
                heapq.heappop(min_heap)
            else:
                heapq.heappush(min_heap, (frequency, num))
        
        result = []

        for frequency, num in min_heap:
            result.append(num)
        
        return result