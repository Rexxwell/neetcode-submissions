class Solution:
    # Brute Force
    # Runtime: 28ms
    # Memory: 7.9 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    #   Because, in the worse case, we only add 1 more element to the digits List[int].
    #   We only consider the extra space the function creates during execution.
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        i = -1
        while (abs(i) != len(digits) and digits[i] == 10):
            digits[i] = 0
            i -= 1
            digits[i] += 1

        if (digits[0] == 10):
            digits[0] = 0
            digits.insert(0, 1)

        return digits