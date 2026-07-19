class Solution:
    # Division Operation and Zero Counting
    # Runtime: 41ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_sum = 1
        zero_count = 0
        
        for num in nums:
            if num != 0:
                total_sum *= num
            else:
                zero_count += 1
        
        output = []

        if zero_count == 0:
            for num in nums:
                output.append(total_sum // num)
        elif zero_count == 1:
            for num in nums:
                if num == 0:
                    output.append(total_sum)
                else:
                    output.append(0)
        else:
            for num in nums:
                output.append(0)
        
        return output