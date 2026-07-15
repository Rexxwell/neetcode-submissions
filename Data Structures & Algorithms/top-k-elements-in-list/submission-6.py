class Solution:
    # Bucket Sort
    # Runtime: 29ms
    # Memory: 8.2 MB
    # Time Complexity: O(n)
    #   The time complexity is not O(nu) where u is the number of unique numbers
    #   in nums because the last loop is an additive not multiplicative.
    #   Nested loops only multiply in time complexity if the inner loop
    #   executes its full length of every iteration of the outern loop.
    #   In this case, we know there will be always O(u) space in result array
    #   since there will always be u unique items in the result array.
    #   Thus, the time complexity on the last loop is O(n + u) = O(n).
    # Space Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        frequent_nums = [[] for _ in range(len(nums) + 1)]

        for num, frequency in nums_dict.items():
            frequent_nums[frequency].append(num)
        
        result = []

        for i in range(len(frequent_nums) - 1, -1, -1):
            for num in frequent_nums[i]:
                result.append(num)
                
                if len(result) == k:
                    return result