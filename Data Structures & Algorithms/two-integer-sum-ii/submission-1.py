class Solution:
    # Brute Force
    # Solution with no AI
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index1 in range(1, len(numbers) + 1):
            for index2 in range(index1 + 1, len(numbers) + 1):
                if numbers[index1 - 1] + numbers[index2 - 1] == target:
                    return [index1, index2]