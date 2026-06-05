class Solution:
    # Brute Force
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if (profit > maxProfit):
                    maxProfit = profit
        return maxProfit