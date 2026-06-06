class Solution:
    # Stack (LIFO)
    # Runtime: 27ms
    # Memory: 7.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, s: str) -> bool:
        # If the length of s is not a multiple of 2,
        # then it is impossible for the string s to be a valid parenthesis.
        # This is because for the string to be a valid parenthesis,
        # it has to have two matching open and closed brackets,
        # meaning that if the string is a valid parenthesis,
        # all the open brackets have its corresponding closed brackets,
        # which means the length of s is always a multiple of 2.
        if (len(s) % 2 == 1):
            return False
        else:
            stack = deque()
            brackets = {"(": ")", "[": "]", "{": "}"}
            for bracket in s:
                # If the bracket is a open bracket,
                # then add it to the stack.
                if (bracket in brackets):
                    stack.append(bracket)
                else:
                    # Else, the bracker has to be a closed bracket,
                    # and if the len(stack) == 0,
                    # that means that there is no corresponding open bracket
                    # for the closed bracket,
                    # which means that string s is not a valid parenthesis.
                    if (len(stack) == 0 
                        or brackets[stack.pop()] != bracket):
                        return False
            # After the loop, if the len(stack) is == 0,
            # then, that means we have appended and popped off
            # all of the corresponding closed and open brackets
            # in the string s.
            # If len(stack) > 0, then that means one of the open or
            # closed brackets did not have its corresponding open or closed bracket.
            if (len(stack) != 0):
                return False
            return True