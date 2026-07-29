class Solution:
    # Two pointer approach
    # Solution with no AI
    # Runtime: 108ms
    # Memory: 8.7 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # This solution uses equation manipulation where you want to
    # simplify this problem into a two pointer approach.
    # Thus, we can make a two pointer approach by making something
    # our target. For example, nums[i] + nums[j] + nums[k] = 0.
    # We can re-write this so that nums[i] = -(nums[j] + nums[k]),
    # -nums[i] = nums[j] + nums[k]. So, now we just need to do the
    # Two Pointer approach for nums[j] and nums[k] where -nums[i]
    # is the target. Don't forget to consider that the indices must
    # be unique where i, j, and k are all unique values.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        distinct_triplets = set()
        i = 0

        while i < len(nums):
            i_target = -nums[i]
            j = 0
            k = len(nums) - 1

            while j < k:
                if k == i or nums[j] + nums[k] > i_target:
                    k -= 1
                elif j == i or nums[j] + nums[k] < i_target:
                    j += 1
                else:
                    distinct_triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                    k -= 1

            i += 1
        
        return [list(triplet) for triplet in distinct_triplets]