import re

class Solution:
    # Brute Force
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isPalindrome(self, s: str) -> bool:
        sWithoutSpaces = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        i = 0
        j = len(sWithoutSpaces) - 1
        while i < j:
            if (sWithoutSpaces[i] != sWithoutSpaces[j]):
                return False
            else:
                i += 1
                j -= 1
        return True
        