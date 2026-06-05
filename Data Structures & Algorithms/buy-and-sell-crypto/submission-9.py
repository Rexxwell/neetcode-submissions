class Solution:
    # Divide and Conquer
    # 3 Scenarios:
    # 1. Both the buy and sell days are in the left half of the array
    # 2. Both the buy and sell days are in the right half of the array
    # 3. You buy somewhere in the left half and sell in the right half of the array
    # Runtime: 41ms
    # Memory: 7.9 MB
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    # Using Master's Theorem, we get a time complexity of O(nlogn) since
    # T(n) = 2T(n/2) + O(n)
    # - n/2 because we are dividing the array by 2 at every level
    # - 2T(n/2) because we are creating 2 subproblems at every level
    # - O(n) because we are doing O(n) work at every level by doing min(pricesLeftHalf)
    #   and max(pricesRightHalf)
    # d = 1
    # logb(a) = log2(2) = 1
    # Since d = logb(a), then the time complexity of this algorithm is O(n^dlogn) = O(nlogn)
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) < 2):
            return 0
        else:
            mid = len(prices) // 2
            pricesLeftHalf = prices[0:mid]
            pricesRightHalf = prices[mid:]
            maxProfitLeftHalf = self.maxProfit(pricesLeftHalf)
            maxProfitRightHalf = self.maxProfit(pricesRightHalf)
            minPriceLeftHalf = min(pricesLeftHalf)
            maxPriceRightHalf = max(pricesRightHalf)
            maxProfitCross = maxPriceRightHalf - minPriceLeftHalf
            return max(maxProfitLeftHalf, maxProfitRightHalf, maxProfitCross)