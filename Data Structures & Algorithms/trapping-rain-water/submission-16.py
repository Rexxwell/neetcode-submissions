class Solution:
    def trap(self, height: List[int]) -> int:
        sz = len(height)
        start = 0
        stop = sz

        print(f"start={start}, stop={stop}, sz={sz}")

        # no water can be trapped at idx == 0 or idx == sz - 1
        # find the heights of the left and right walls at each index
        # iterate through the array twice

        left_walls = [0] * sz
        for i in range(start, stop, 1):
            if (i == 0):
                left_walls[i] = height[i]
            else:
                left_walls[i] = max(height[i], left_walls[i - 1])

            print(f"left_walls[{i}] = {left_walls[i]}")
        
        right_walls = [0] * sz
        for i in range(stop - 1, start, -1):
            if (i == sz - 1):
                right_walls[i] = height[i]
            else:
                right_walls[i] = max(height[i], right_walls[i + 1])
            print(f"right_walls[{i}] = {right_walls[i]}")

        total = 0
        for i in range(start, stop):
            water_at_i = min(left_walls[i], right_walls[i]) - height[i]
            if water_at_i > 0:
                total += water_at_i

        return total
            

            
