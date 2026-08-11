class Solution:
    # Stack
    # Runtime: 83ms
    # Memory: 21.3 MB
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []

        for i in range(len(position)):
            position_speed.append([position[i], speed[i]])
        
        position_speed.sort()
        stack = []
        time = (target - position_speed[-1][0]) / position_speed[-1][1]
        stack.append(time)

        for i in range(len(position_speed) - 2, -1, -1):
            time = (target - position_speed[i][0]) / position_speed[i][1]

            if time > stack[-1]:
                stack.append(time)

        return len(stack)