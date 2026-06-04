class Solution:
    # Stack Approach (LIFO)
    def isPalindrome(self, s: str) -> bool:
        stack = deque()
        sCleaned = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        sCleanedLength = len(sCleaned)
        mid = sCleanedLength // 2
        for i in range(mid):
            stack.append(sCleaned[i])
        startIndex = mid  if sCleanedLength % 2 == 0 else mid + 1
        for i in range(startIndex, sCleanedLength):
            if (sCleaned[i] != stack.pop()):
                return False
        return True
        