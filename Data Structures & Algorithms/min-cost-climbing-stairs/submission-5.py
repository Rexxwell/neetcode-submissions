class Solution:
    # Brute Force (Recursion)
    # Runtime: Time Limit Exceeded
    # Memory: N/A
    # Time Complexity: O(2^n)
    #   Because every recursive calls will call two more recursive calls.
    # Space Complexity: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.minCostClimbingStairsHelper(cost, len(cost))

    def minCostClimbingStairsHelper(self, cost: List[int], step: int) -> int:
        if step == 0 or step == 1:
            return 0
        return min(
            self.minCostClimbingStairsHelper(cost, step - 1) + cost[step - 1],
            self.minCostClimbingStairsHelper(cost, step - 2) + cost[step - 2]
        )
