class Solution:
    # Sorting
    # Runtime: 42ms
    # Memory: 7.9 MB
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndexPairs = [(num, i) for i, num in enumerate(nums)]
        numIndexPairs.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            ijSum = numIndexPairs[i][0] + numIndexPairs[j][0]
            if (ijSum == target):
                return sorted([numIndexPairs[i][1], numIndexPairs[j][1]])
            elif (ijSum > target):
                j -= 1
            else:
                i += 1
        return []