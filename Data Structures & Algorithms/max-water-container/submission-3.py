class Solution:
    # Two pointer algorithm
    # Runtime: 41ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # By moving the pointer of the index that has the smaller
    # height, it is the only move that has a mathematical chance
    # where there is a possibility to increase the volume of the
    # water. Whereas, if you moved the pointer with the higher
    # height, then we are decreasing the maximum volume we can
    # we can get. Thus, there is only one move that has a
    # mathematical chance to increase the volume of the water.
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            water = (j - i) * min(heights[i], heights[j])

            if water > max_water:
                max_water = water

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_water
        