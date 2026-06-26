class Solution:
    # Floyd's Cycle-Finding Algorithm
    # Runtime: 28ms
    # Memory: 7.7 MB
    # Time Complexity: log(n)
    # Space Complexity: O(1)
    def isHappy(self, n: int) -> bool:
        slowPointer = n
        fastPointer = self.isHappyHelper(n)
        while (fastPointer != 1 and slowPointer != fastPointer):
            """
            If the fastPointer == 1, then n is a non-cyclical number.
            If the slowPointer == fastPointer, then n is not a non-cylical number
            because there is a cycle since the fastPointer caught up with the slowPointer.
            """
            slowPointer = self.isHappyHelper(slowPointer)
            fastPointer = self.isHappyHelper(self.isHappyHelper(fastPointer))
        
        return fastPointer == 1
        
    def isHappyHelper(self, n: int) -> int:
        sumOfSquare = 0
        while (n > 0):
            digit = n % 10
            sumOfSquare += digit ** 2
            n //= 10
            
        return sumOfSquare