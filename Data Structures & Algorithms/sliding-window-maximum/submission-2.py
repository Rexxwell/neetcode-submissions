import heapq

class Solution:
    # Max heap
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements = []
        i = 0
        j = k - 1
        window = []

        for l in range(i, j + 1):
            heapq.heappush(window, (-nums[l], l))

        max_elements.append(-window[0][0])
            
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