import re

class Solution:
    # Brute Force
    def isPalindrome(self, s: str) -> bool:
        sWithoutSpaces = re.sub(r"[^a-zA-Z0-9]", "", s).replace(" ", "").lower()
        i = 0
        j = len(sWithoutSpaces) - 1
        while i < j:
            if (sWithoutSpaces[i] != sWithoutSpaces[j]):
                return False
            else:
                i += 1
                j -= 1
        return True
        