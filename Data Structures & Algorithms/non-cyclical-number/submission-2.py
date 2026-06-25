class Solution:
    # Brute Force
    # Runtime: 29ms
    # Memory: 7.7 MB
    # Time Complexity: O(log n)
    #   The time complexity of this function is determined the number
    #   times the while loop loops, in this function,
    #   the while loop loops depending on the number of digits in n.
    #   Thus, there are roughly log10(n) digits in n. So, the time complexity is O(logn)
    # Space Complexity: O(1)
    #   This is because the space memory hits a ceiling and stops growing no matter
    #   how big the input is. The max number is 999, which is (9^2)^3 = 243.
    #   Because the maximum possible size of the set is being limited by the rules of math
    #   where the maximum possible size of the set is 243. The space complexity is O(1).
    def isHappy(self, n: int) -> bool:
        sumOfSquares = set()
        while n != 1 and n not in sumOfSquares:
            sumOfSquares.add(n)

            sumOfSquare = 0
            while (n > 0):
                digit = n % 10
                sumOfSquare += digit ** 2
                n //= 10
            
            n = sumOfSquare
        return n == 1