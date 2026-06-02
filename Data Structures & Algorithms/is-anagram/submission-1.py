class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If both strings don't have the same length,
        # then it is impossible both strings to be anagrams of each other.
        if (len(s) != len(t)):
            return False
        sCopy = s
        tCopy = t
        for sChar in s:
            for tChar in t:
                if (sChar == tChar):
                    sCopy = sCopy.replace(sChar, "", 1)
                    tCopy = tCopy.replace(tChar, "", 1)
                    break
        return (len(sCopy) == 0) and (len(tCopy) == 0)