class Solution:
    # Divide and Conquer (Masking)
    # Instead of moving the bits one by one, we swap them in blocks
    # simultaneously using hex masks
    # Runtime: 43ms
    # Memory: 8.0 MB
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def reverseBits(self, n: int) -> int:
        # Swap 1-bit blocks
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)

        # Swap 2-bit blocks
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2)

        # Swap 4-bit blocks
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4)

        # Swap 8-bit blocks
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8)

        # Swap 16-bit blocks
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)

        return n