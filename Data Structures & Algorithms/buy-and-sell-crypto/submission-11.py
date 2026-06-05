class Solution:
    # Greedy Algorithm
    # Runtime: 37ms
    # Memory: 8.0 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            if (price < minPrice):
                minPrice = price
            elif (price - minPrice > maxProfit):
                maxProfit = price - minPrice
        return maxProfit