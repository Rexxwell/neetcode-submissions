class Solution:
    # Bit Shifting
    # Runtime: 45ms
    # Memory: 8.3 MB
    # Time Complexity: O(32) = O(1)
    #   Since the constraint is that n is a non-negative integer which fits within 32 bits
    # Space Complexity: O(1)
    def hammingWeight(self, n: int) -> int:
        res = 0
        while (n > 0):
            if (n & 1 == 1):
                res += 1
            n >>= 1

        return res