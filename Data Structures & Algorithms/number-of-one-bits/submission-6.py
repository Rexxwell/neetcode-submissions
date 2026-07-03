class Solution:
    # Brian Kernighan's Algorithm
    # If you take any binary number n and subtract 1 from it,
    # all the bits from the rightmost 1 to the end of the number will flip
    # from a 0 to a 1. If you do this and do a bitwise AND with
    # n and n-1, it will erase the rightmost 1 bit of n.
    # Runtime: 27ms
    # Memory: 7.7 MB
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while (n > 0):
            n = n & (n-1)
            counter += 1
        
        return counter