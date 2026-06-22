class Solution:
    # Top-Down Dynamic Programming (Memoization)
    # Runtime: 48ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    #   By implementing the minCosts dictionary, we reduce the time complexity from O(2^m)
    #   to O(n) because it will only compute each step at most once.
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCosts = {0: 0, 1: 0}
        step = len(cost)
        return self.minCostClimbingStairsHelper(cost, step, minCosts)

    def minCostClimbingStairsHelper(self, cost: List[int], step: int, minCosts: dict[int, int]) -> int:
        if (step in minCosts):
            return minCosts[step]
        minCost = min(
                self.minCostClimbingStairsHelper(cost, step - 1, minCosts) + cost[step - 1],
                self.minCostClimbingStairsHelper(cost, step - 2, minCosts) + cost[step - 2]
            )
        minCosts[step] = minCost
        return minCost