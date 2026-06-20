class Solution:
    # Dynamic Programming With Space Optimization
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        nMinus1 = 2
        nMinus2 = 1
        steps = 0
        for i in range(2, n):
            steps = nMinus1 + nMinus2
            nMinus2 = nMinus1
            nMinus1 = steps
        return steps