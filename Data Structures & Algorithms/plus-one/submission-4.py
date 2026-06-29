class Solution:
    # Iterative Approach (for loop)
    # Runtime: 27ms
    # Memory: 7.9 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if (digits[i] < 9):
                '''
                if digits[i] < 9, then that means there is no carry over.
                So, just return the digits after incrementing it by one.
                '''
                digits[i] += 1
                return digits
            '''
            if digits[i] >= 9, then that means ther is carry over.
            So, we just set digits[i] = 0 and don't increment digits[i-1] by 1
            because we will increment it by 1 in the next iteration.
            '''
            digits[i] = 0

        '''
        if it does not return after the for loop, that means that the number
        is all 9's in all digits and now, the digits[i] would be all 0's.
        That means we need to only insert a 1 to the left as the carry over.
        '''
        return [1] + digits