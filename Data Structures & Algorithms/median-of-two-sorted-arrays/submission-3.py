class Solution:
    # Brute Force
    # Runtime: 28ms
    # Memory: 7.9 MB
    # Time Complexity: O(nm)
    # Space Complexity: O(nm)
    # n is the length of nums1
    # m is the length of nums2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return float('nan')

        nums1_2 = nums1 + nums2
        nums1_2.sort()
        low = 0
        high = len(nums1_2) - 1
        if len(nums1_2) % 2 == 0:
            mid = low + (high - low) // 2
            return (nums1_2[mid] + nums1_2[mid + 1]) / 2
        else:
            mid = low + (high - low) // 2
            return nums1_2[mid]