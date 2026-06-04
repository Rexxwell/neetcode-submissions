import re

class Solution:
    # Comparing the reverse string
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(1)
    # Space Complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        sCleaned = re.sub(r"[^a-zA-z0-9]", "", s).lower()
        sCleanedReverse = sCleaned[::-1]
        return sCleaned == sCleanedReverse