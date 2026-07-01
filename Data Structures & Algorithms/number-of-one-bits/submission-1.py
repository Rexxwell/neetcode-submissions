class Solution:
    # .bit_count()
    # Runtime: 26ms
    # Memory: 7.7 MB
    # Time Complexity: O(1) or O(k) where k is the number of bits = 32
    # Space Complexity: O(1)
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()