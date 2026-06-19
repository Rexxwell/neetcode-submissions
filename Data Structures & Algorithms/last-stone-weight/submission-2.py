class Solution:
    # Brute Force
    # Runtime: 30ms
    # Memory: 7.9 MB
    # Time Complexity:
    #   Best Case: O(n^2logn)
    #   Worst Case: O(n^2)
    #   Python .sort() uses Timsort where in the worst case, takes O(nlogn) time.
    #   Average case, takes O(nlogn) time. Best case, takes O(n) time.
    # Space Complexity: O(n)
    #   Python .sort() uses O(n/2) = O(n) time to merge the arrays together.
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) >= 2):
            stones.sort()
            x = stones[-2]
            y = stones[-1]
            diff = abs(x - y)
            if (diff == 0):
                stones.pop()
                stones.pop()
            elif (diff > 0):
                stones.pop()
                stones[-1] = diff
        return 0 if len(stones) == 0 else stones[0]