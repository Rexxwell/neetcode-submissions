class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 == 1):
            return False
        else:
            stack = deque()
            brackets = {"(": ")", "[": "]", "{": "}"}
            for bracket in s:
                if (bracket in brackets.keys()):
                    stack.append(bracket)
                elif (bracket in brackets.values()):
                    if (len(stack) == 0 
                        or brackets[stack.pop()] != bracket):
                        return False
            if (len(stack) != 0):
                return False
            return True