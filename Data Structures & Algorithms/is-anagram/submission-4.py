class Solution:
    # Dictionary V2
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for sChar in s:
            sDict[sChar] = sDict.get(sChar, 0) + 1
        for tChar in t:
            tDict[tChar] = tDict.get(tChar, 0) + 1
        return sDict == tDict