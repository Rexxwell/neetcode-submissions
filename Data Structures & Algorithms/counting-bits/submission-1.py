class Solution:
    # Brian Kernighan's Algorithm
    # Runtime: 30ms
    # Memory: 7.7 MB
    # Time Complexity: O(nlogn)
    #   The for loop runs n+1 times from 0 to n, so the time complexity is O(n)
    #   The while loop uses Brian Kernighan's Algorithm to only loop by the number
    #   of 1 bits in i. So, the maximum number of bits required to represent an integer n
    #   in binary is log2(n). Therefore, the worse case is O(logn).
    # Space Complexity: O(n)
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            counter = 0
            while (i > 0):
                i = i & (i - 1)
                counter += 1
            output.append(counter)
        
        return output