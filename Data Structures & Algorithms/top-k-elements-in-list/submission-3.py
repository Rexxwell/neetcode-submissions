class Solution:
    # Dictionary and Sorting
    #   `key=lambda x: frequent_nums[x]` works where the sorted() function would
    #   sort the frequent_nums dictionary by the value of the keys in descending order.
    # Runtime: 33ms
    # Memory: 8.0 MB
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_nums = {}
        for num in nums:
            if num in frequent_nums:
                frequent_nums[num] += 1
            else:
                frequent_nums[num] = 1
        
        sorted_keys = sorted(frequent_nums.keys(), key=lambda x: frequent_nums[x], reverse=True)

        return sorted_keys[:k]