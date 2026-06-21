class Solution:
    # Dynamic Programming
    # Runtime: 39ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimumCosts = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            minimumCosts[i] = min(minimumCosts[i-1] + cost[i-1], minimumCosts[i-2] + cost[i-2])
        return minimumCosts[len(cost)]