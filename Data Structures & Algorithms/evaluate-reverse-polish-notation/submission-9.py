class Solution:
    # Stack
    # Runtime: 150ms
    # Memory: 10.7 MB
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0

        while i < len(tokens):
            token = tokens[i]

            if token in "+-*/":
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                result = 0

                if token == "+":
                    result = operand_1 + operand_2
                elif token == "-":
                    result = operand_1 - operand_2
                elif token == "*":
                    result = operand_1 * operand_2
                elif token == "/":
                    result = int(operand_1 / operand_2)
                
                stack.append(result)
            else:
                stack.append(token)
            
            i += 1

        return int(stack.pop())