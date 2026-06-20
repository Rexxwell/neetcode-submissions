class Solution:
    # Top-Down DP (Memoization)
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    #   Total Time = (Number of unique subproblems) x (Time to solve each subproblem)
    #              = n x O(1)
    #              = O(n)
    # Space Complexity: O(n)
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        return self.climbStairsHelper(n, memo)
        
    def climbStairsHelper(self, n: int, memo: dict[int, int]) -> int:
        if (n in memo):
            return memo[n]
        else:
            memo[n] = self.climbStairsHelper(n-1, memo) + self.climbStairsHelper(n-2, memo)
            return memo[n]