import heapq

class Solution:
    # Max heap
    # Runtime: 116ms
    # Memory: 22.2 MB
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    # n is the length of nums.
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements = []
        i = 0
        j = k - 1
        window = []

        # O(klogk)
        for l in range(i, j + 1):
            heapq.heappush(window, (-nums[l], l))

        max_elements.append(-window[0][0])
            
        # O(nlogn)
        while j < len(nums) - 1:
            j += 1
            heapq.heappush(window, (-nums[j], j))

            # Check if the current max element in the window is in the
            # current window.
            i += 1
            max_element_index = window[0][1]

            while max_element_index < i:
                heapq.heappop(window)
                max_element_index = window[0][1]
            
            # Found a max element in the window that is in the current
            # window.
            max_elements.append(-window[0][0])

        return max_elements