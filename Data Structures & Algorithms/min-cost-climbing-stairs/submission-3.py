class Solution:
    # Dynamic Programming With Space Optimization O(1)
    # Runtime: 32ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stepIMinus1 = 0
        stepIMinus2 = 0
        minimumCost = 0
        for i in range(2, len(cost) + 1):
            minimumCost = min(stepIMinus1 + cost[i-1], stepIMinus2 + cost[i-2])
            stepIMinus2 = stepIMinus1
            stepIMinus1 = minimumCost
        return minimumCost