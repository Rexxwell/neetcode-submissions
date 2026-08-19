class Solution:
    # Binary Search
    # The goal of this solution is to create two partitions,
    # left and right, where we want to make it where the length of the
    # left partition is the same or contains one extra element
    # (for odd merged array lengths) than the right partition and
    # the maximum element on the combined left partition on A and B
    # are lesser than the minimum element on the combined right
    # partition on A and B.
    # Runtime: 29ms
    # Memory: 8.0 MB
    # Time Complexity: O(log(n + m))
    # Space Complexity: O(1) auxiliary space, O(n + m)
    # n is the length of nums1
    # m is the length of nums2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        # A must be the smaller array size because this guarantees that
        # half - i will stay strictly within [0, len(B)].
        # We will run into an index out-of-bounds error if we set A
        # to be the larger array.
        if len(nums2) < len(nums1):
            A, B = nums2, nums1

        # If len(A) + len(B) is odd, then the left partition will
        # contain one extra element, where the median lies.
        # If len(A) + len(B) is even, then the left and right partition
        # will contain the same number of elements, where the median
        # has to be computed.
        half = (len(A) + len(B) + 1) // 2
        low = 0
        high = len(A)

        while low <= high:
            A_mid = low + (high - low) // 2
            B_mid = half - A_mid
            A_left_max = A[A_mid - 1] if A_mid > 0 else float("-inf")
            A_right_min = A[A_mid] if A_mid < len(A) else float("inf")
            B_left_max = B[B_mid - 1] if B_mid > 0 else float("-inf")
            B_right_min = B[B_mid] if B_mid < len(B) else float("inf")

            if A_left_max <= B_right_min and B_left_max <= A_right_min:
                # All of the elements on the left partition on A and B
                # combined are lesser than the minimum element on the
                # right partition on A and B combined. Thus, we have
                # found a valid partition.
                
                if (len(A) + len(B)) % 2 == 0:
                    return (max(A_left_max, B_left_max) + min(A_right_min, B_right_min)) / 2
                else:
                    return max(A_left_max, B_left_max)
            elif A_left_max > B_right_min:
                # We have to pick lesser elements in A and more from B.

                high = A_mid - 1
            elif B_left_max > A_right_min:
                # We have to pick more elements in A and less from B.

                low = A_mid + 1