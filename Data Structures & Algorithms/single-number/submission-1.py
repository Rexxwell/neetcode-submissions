class Solution:
    # XOR
    # Runtime: 28ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Using XOR works because of the properties of XOR.
        x ^ x = 0 (Any number XORed with itself results to 0)
        x ^ 0 = x (Any number XORed with 0 results to the same number)
        This works because for every pair of numbers,
        it will XOR with itself, thus cancelling each other and
        resulting to 0. While, the only number that appears once
        will XOR with 0 and will result to the number.

        Intuitively, this might not work because of the order on how
        the XOR happens, for example, if the list is [7, 1, 6, 6, 7],
        then you would think that 7 XOR 1 would break everything but
        there is a property of XOR where
        7 XOR 1 XOR 6 XOR 6 XOR 7 = 7 XOR 7 XOR 6 XOR 6 XOR 1 = 0 XOR 0 XOR 1 = 1
        This is the commutative and associative property where the order in
        which you XOR numbers do not matter.
        '''
        result = 0
        for num in nums:
            result ^= num
        return result