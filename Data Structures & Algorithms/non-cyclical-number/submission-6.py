class Solution:
    # Hardcoded Cycle Approach
    # All numbers that are cyclical will follow the same sequence of numbers cycle.
    # The sequence is 4, 16, 37, 58, 89, 145, 42, 20, 4, ...
    # Runtime: 27ms
    # Memory: 8.0 MB
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    def isHappy(self, n: int) -> bool:
        while (n != 1 and n != 4):
            sumOfSquare = 0
            while (n > 0):
                digit = n % 10
                n //= 10
                sumOfSquare += digit ** 2
            n = sumOfSquare
        return n == 1