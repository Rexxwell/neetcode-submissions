class Solution:
    # Binary Search
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = 1
        k_max = max(piles)

        while k_min <= k_max:
            mid = k_min + (k_max - k_min) // 2
            h_taken = 0

            for pile in piles:
                h_taken += math.ceil(pile / mid)
            
            if h_taken == h:
                k_max = mid - 1
            elif h_taken > h:
                k_min = mid + 1
            elif h_taken < h:
                k_max = mid - 1
            
        return k_min