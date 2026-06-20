class Solution:
    # Dynamic Programming
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def climbStairs(self, n: int) -> int:
        steps = []
        steps.append(1)
        steps.append(2)
        for i in range(2, n):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n-1] 