class Solution:
    # Fixed Array
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        charCounts = [0] * 26
        for sChar in s:
            charCounts[ord(sChar) - ord("a")] += 1
        for tChar in t:
            charCounts[ord(tChar) - ord("a")] -= 1
        for charCount in charCounts:
            if (charCount != 0):
                return False
        return True