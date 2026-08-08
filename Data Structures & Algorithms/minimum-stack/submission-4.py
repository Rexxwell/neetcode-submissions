class MinStack:
    # History Log Extra Stack
    # Runtime: 61ms
    # Memory: 11.7 MB
    # Time Complexity: O(1)
    # Space Complexity: O(n)

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        del self.main_stack[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
