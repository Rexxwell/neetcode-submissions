class Solution:
    # Manual bit reversing
    # Runtime: 28ms
    # Memory: 7.7 MB
    # Time Complexity: O(1) or O(32)
    # Space Complexity: O(1)
    def reverseBits(self, n: int) -> int:
        reverse_n = 0
        for i in range(32):
            bit = n & 1
            reverse_n <<= 1
            reverse_n |= bit
            n >>= 1
        
        return reverse_n