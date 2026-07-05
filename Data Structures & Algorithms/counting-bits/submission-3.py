class Solution:
    # Manual Bit Checking
    # Runtime: 30ms
    # Memory: 7.7 MB
    # Time Complexity: O(nlog(n))
    # Space Complexity: O(n)
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            result = 0
            while (i > 0):
                if (i % 2 == 1):
                    result += 1
                i >>= 1
            output.append(result)
        return output