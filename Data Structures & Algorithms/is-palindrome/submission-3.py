class Solution:
    # Two Pointer With Space Efficiency
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while (i < j):
            if (not s[i].isalnum()):
                i += 1
            elif (not s[j].isalnum()):
                j -= 1
            elif (s[i].lower() != s[j].lower()):
                return False
            else:
                i += 1
                j -= 1
        return True
        