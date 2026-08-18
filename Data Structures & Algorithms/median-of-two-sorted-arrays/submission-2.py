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

        nums1_2 = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            nums1_i = nums1[i]
            nums2_j = nums2[j]

            if nums1_i == nums2_j:
                nums1_2.append(nums1_i)
                nums1_2.append(nums2_j)
                i += 1
                j += 1
            elif nums1_i > nums2_j:
                nums1_2.append(nums2_j)
                j += 1
            elif nums1_i < nums2_j:
                nums1_2.append(nums1_i)
                i += 1
        
        while i < len(nums1):
            nums1_2.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            nums1_2.append(nums2[j])
            j += 1

        low = 0
        high = len(nums1_2) - 1
        if len(nums1_2) % 2 == 0:
            mid = low + (high - low) // 2
            return (nums1_2[mid] + nums1_2[mid + 1]) / 2
        else:
            mid = low + (high - low) // 2
            return nums1_2[mid]