class Solution:
    # Brute Force
    # Solution with no AI
    # Runtime: Time Limit Exceeded
    # Memory: Time Limit Exceeded
    # Time Complexity: O(n^3)
    # Space Complexity: O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        distinct_triplets = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        distinct_triplets.add((nums[i], nums[j], nums[k]))
        
        return [list(triplet) for triplet in distinct_triplets]