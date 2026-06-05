class Solution:
    # Two Pointers
    # Runtime: 29ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        while (right < len(prices)):
            if (prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                if (profit > maxProfit):
                    maxProfit = profit
            # Found a better buy day that is lower in price.
            if (prices[right] < prices[left]):
                left = right
            right += 1
        return maxProfit
