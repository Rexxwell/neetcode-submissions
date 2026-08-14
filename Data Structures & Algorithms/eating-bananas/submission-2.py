class Solution:
    # Brute Force
    # Runtime: 1096ms
    # Memory: 8.2 MB
    # Time Complexity: O(n ^2)
    # Space Complexity: O(1)
    # n is the length of piles.
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)

        if h == len(piles):
            return k_max

        for i in range(k_max, k_min - 1, -1):
            h_taken = 0

            for pile in piles:
                h_taken += math.ceil(pile / i)

            if h_taken > h:
                return i + 1
        
        return k_min