class MinStack:
    # Brute Force
    # Runtime: 2451ms
    # Memory: 11.6 MB

    # O(1)
    def __init__(self):
        self.min_stack = []

    # O(1)
    def push(self, val: int) -> None:
        self.min_stack.append(val)

    # O(1)
    def pop(self) -> None:
        del self.min_stack[-1]

    # O(1)
    def top(self) -> int:
        return self.min_stack[-1]

    # O(n)
    def getMin(self) -> int:
        min_val = min(self.min_stack)

        return min_val
