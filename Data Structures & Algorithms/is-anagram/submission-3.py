class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {}
        for sChar in s:
            charDict[sChar] = charDict.get(sChar, 0) + 1
        for tChar in t:
            if (tChar not in charDict):
                return False
            charDict[tChar] = charDict.get(tChar, 0) + 1
        for value in charDict.values():
            if (value % 2 == 1):
                return False
        return True
